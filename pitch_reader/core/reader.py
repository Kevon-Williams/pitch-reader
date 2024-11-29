import time
import threading
from asyncio import QueueEmpty
from concurrent.futures import ThreadPoolExecutor
from collections import deque
import numpy as np
from mss.windows import MSS as mss
from torch.multiprocessing.queue import Queue

from pitch_reader.services.audio import Audio
from pitch_reader.services.ocr import Ocr
from pitch_reader.core.config import ScreenConfig
from pitch_reader.core.generate_text import Commentary

class ScreenReader:
    """
    ScreenReader class to read the screen and generate commentary

    """
    def __init__(self, buffer_size=10):
        self.screen_config = ScreenConfig()
        self.previous_texts = deque(maxlen=buffer_size) # Set the size of the context
        self.commentary = Commentary()
        self.audio_service = Audio()
        self.ocr = Ocr()

        self.image_queue = Queue(maxsize=5)
        self.text_queue = Queue(maxsize=5)
        self.commentary_queue = Queue(maxsize=5)

        self.running = False
        self.threads = []
        self.executor = ThreadPoolExecutor(max_workers=3)

    def capture_screen(self):
        """Thread 1: Continuously captures screenshots and adds to image queue"""
        with mss as sct:
            while self.running:
                screenshot = sct.grab(self.screen_config.resolution())
                self.image_queue.put(np.array(screenshot)) #puts image in queue
                time.sleep(0.1)  # Prevent CPU overload

    def process_ocr(self):
        """Thread 2: Processes screenshots with OCR and adds unique text to text queue"""
        while self.running:
            if QueueEmpty:
                continue
            image = self.image_queue.get(timeout=1) # Get image from queue
            text = self.ocr.process_image(image) # Process image

            if text and text not in self.previous_texts: # Check if text is unique
                self.text_queue.put(text)
                self.previous_texts.append(text)

    def generate_commentary(self):
        """Thread 3: Generates commentary and adds to commentary queue"""
        while self.running:
            if QueueEmpty:
                continue

            text = self.text_queue.get(timeout=1)
            commentary = self.commentary.generate_commentary(text)
            self.commentary_queue.put(commentary)

    def play_audio(self):
        """Thread 4: Plays audio from commentary queue"""
        while self.running:
            if QueueEmpty:
                continue

            commentary = self.commentary_queue.get(timeout=1)
            self.audio_service.start_audio_stream(commentary)


    def start(self):
        """Starts all threads"""
        self.running = True




    # def process_text(self, text):
    #     """
    #     Processes the text and generates commentary
    #     :param text:
    #     :return:
    #     """
    #     if not text or text in self.previous_texts: # Skip if text is empty or already processed
    #         return
    #
    #     self.previous_texts.append(text)
    #     new_commentary = self.commentary.generate_commentary(text) # Generate commentary
    #
    #     print(f"Processing: {new_commentary}")
    #     self.audio_service.start_audio_stream(new_commentary) # play audio
    #
    # def take_screenshot_and_process(self, duration, sleep_time=5):
    #     """
    #     Takes a screenshot and processes the text
    #     :param duration: int: duration in seconds to run the program
    #     :param sleep_time: int: time to sleep between screenshots
    #     """
    #     start_time = time.time()
    #
    #
    #     with mss() as sct:
    #         while (time.time() - start_time) < duration:
    #             screenshot = sct.grab(self.screen_config.resolution())
    #             img_array = np.array(screenshot) #convert to np array for processing
    #             text = self.ocr.process_image(img_array) #Get text from image
    #             self.process_text(text)
    #             time.sleep(sleep_time)
    #
    #
    #
    # def close_audio_stream(self):
    #     """Closes the audio stream"""
    #     self.audio_service.stop_audio()
    #     print("Audio stream closed")

