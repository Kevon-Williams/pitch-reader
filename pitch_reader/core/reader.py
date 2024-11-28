import time
from collections import deque
import numpy as np
from mss.windows import MSS as mss

from pitch_reader.services.audio import Audio
from pitch_reader.services.ocr import Ocr
from pitch_reader.core.config import ScreenConfig
from pitch_reader.core.generate_text import Commentary

class ScreenReader:
    """
    ScreenReader class to read the screen and generate commentary

    """
    def __init__(self, screen_config=None, buffer_size=10):
        self.screen_config = ScreenConfig()
        self.previous_texts = deque(maxlen=buffer_size) # Set the size of the context
        self.commentary = Commentary()
        self.audio_service = Audio()
        self.ocr = Ocr()

    def process_text(self, text):
        """
        Processes the text and generates commentary
        :param text:
        :return:
        """
        if not text or text in self.previous_texts: # Skip if text is empty or already processed
            return

        self.previous_texts.append(text)
        new_commentary = self.commentary.generate_commentary(text) # Generate commentary

        print(f"Processing: {new_commentary}")
        self.audio_service.start_audio_stream(new_commentary) # play audio

    def take_screenshot_and_process(self, duration, sleep_time=5):
        """
        Takes a screenshot and processes the text
        :param duration: int: duration in seconds to run the program
        :param sleep_time: int: time to sleep between screenshots
        """
        start_time = time.time()


        with mss() as sct:
            while (time.time() - start_time) < duration:
                screenshot = sct.grab(self.screen_config.resolution())
                img_array = np.array(screenshot) #convert to np array for processing
                text = self.ocr.process_image(img_array) #Get text from image
                self.process_text(text)
                time.sleep(sleep_time)



    def close_audio_stream(self):
        """Closes the audio stream"""
        self.audio_service.stop_audio()
        print("Audio stream closed")

