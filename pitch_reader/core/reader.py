import time
from collections import deque
import numpy as np
from mss.windows import MSS

from pitch_reader.services.audio import Audio
from pitch_reader.services.ocr import Ocr
from pitch_reader.core.config import ScreenConfig


class ScreenReader:
    """
    ScreenReader class to read the screen and generate commentary
    """
    def __init__(self, buffer_size=10):
        self.screen_config = ScreenConfig()
        self.previous_texts = deque(maxlen=buffer_size)  # Set the size of the context
        #self.commentary = Commentary()
        self.audio_service = Audio()
        self.ocr = Ocr()

        self.most_recent_image = None
        self.most_recent_text= None

        self.running = False



    def capture_screen(self):
        """
        captures screenshot and stores it in self.latest_image
        :param:
        :return:
        """
        with MSS() as sct:
                screenshot = sct.grab(self.screen_config.resolution())
                self.most_recent_image = np.array(screenshot)
                #time.sleep(3)  # seconds between screenshots

    def process_ocr(self):
        """
        gets text from the latest image using OCR
        :param:
        :return:
        """
        if self.most_recent_image is not None:
            text = self.ocr.process_image(self.most_recent_image)

            if text and text not in self.previous_texts:  # check if text is unique
                self.most_recent_text = text
                self.previous_texts.append(text)
        self.most_recent_image = None



    def play_audio(self):
        """
        plays the most recent commentary
        :param:
        :return:
        """
        if self.most_recent_text is not None:
            self.audio_service.start_audio_stream(self.most_recent_text)
            print(f"Playing: {self.most_recent_text}")

        self.most_recent_text = None


    def start(self, duration):
        """
        starts processing
        :param duration: int: duration in seconds to run the program
        :return:
        """
        self.running = True
        start_time = time.time()
        while self.running and (time.time() - start_time) < duration:
            self.capture_screen()
            self.process_ocr()
            # self.generate_commentary()
            self.play_audio()

            time.sleep(1) # seconds between cycles


    def stop(self):
        """stop function"""
        self.running = False