import time
import threading
from queue import Empty as QueueEmpty
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from queue import Queue as StdQueue
import numpy as np
from mss.windows import MSS

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
        self.previous_texts = deque(maxlen=buffer_size)  # Set the size of the context
        self.commentary = Commentary()
        self.audio_service = Audio()
        self.ocr = Ocr()

        self.text_batch = []
        self.batch_size = 2 # Number of texts to batch before generating commentary

        self.image_queue = StdQueue(maxsize=5)
        self.text_queue = StdQueue(maxsize=5)
        self.commentary_queue = StdQueue(maxsize=5)

        self.running = False
        self.threads = []
        self.executor = ThreadPoolExecutor(max_workers=3)

    def capture_screen(self):
        """Thread 1: Continuously captures screenshots and adds to image queue"""
        with MSS() as sct:
            while self.running:
                screenshot = sct.grab(self.screen_config.resolution())
                self.image_queue.put(np.array(screenshot))  # puts image in queue
                time.sleep(5)  # seconds between screenshots

    def process_ocr(self):
        """Thread 2: Processes screenshots with OCR and adds unique text to text queue"""
        while self.running:
            try:
                image = self.image_queue.get(timeout=1)  # Get image from queue
                text = self.ocr.process_image(image)  # Process image

                if text and text not in self.previous_texts:  # Check if text is unique
                    self.text_queue.put(text)
                    self.previous_texts.append(text)
            except QueueEmpty:
                continue

    def generate_commentary(self):
        """Thread 3: Generates commentary and adds to commentary queue"""
        while self.running:
            try:
                text = self.text_queue.get(timeout=1)
                commentary = self.commentary.generate_commentary(text)
                self.commentary_queue.put(commentary)

            except QueueEmpty:
                continue

    def play_audio(self):
        """Thread 4: Plays audio from commentary queue"""
        while self.running:
            try:
                commentary = self.commentary_queue.get(timeout=1)
                self.audio_service.start_audio_stream(commentary)
                print(f"Playing: {commentary}")
            except QueueEmpty:
                continue

    def start(self, duration):
        """Starts all threads"""
        self.running = True

        self.threads = [
            threading.Thread(target=self.capture_screen),
            threading.Thread(target=self.process_ocr),
            threading.Thread(target=self.generate_commentary),
            threading.Thread(target=self.play_audio)
        ]

        for thread in self.threads:
            thread.start()

        time.sleep(duration)
        self.stop()

    def stop(self):
        """Stops threads and cleanup"""
        self.running = False

        for thread in self.threads:
            thread.join()

        self.audio_service.stop_audio()
        self.executor.shutdown()