import time
from collections import deque
import numpy as np
from mss.windows import MSS as mss

from pitch_reader.services.audio import Audio
from pitch_reader.services.ocr import Ocr
from pitch_reader.services.tts import TTS
from pitch_reader.core.config import ScreenConfig

class ScreenReader:
    def __init__(self, api_key, screen_config=None, buffer_size=5):
        self.screen_config = ScreenConfig()
        self.previous_texts = deque(maxlen=buffer_size)

        self.audio_service = Audio()
        self.ocr = Ocr()
        self.tts = TTS(api_key)

    def process_text(self, text):
        if not text or text in self.previous_texts:
            return

        self.previous_texts.append(text)
        print(f"Processing: {text}")

        try:
            for chunk in self.tts.text_to_speech(text):
                self.audio_service.write_chunk(chunk)
        except Exception as e:
            print(f"Error processing text: {e}")

    def take_screenshot_and_process(self, duration):
        self.audio_service.start_audio_stream()
        start_time = time.time()

        with mss() as sct:
            while (time.time() - start_time) < duration:
                screenshot = sct.grab(self.screen_config.resolution())
                img_array = np.array(screenshot)
                text = self.ocr.process_image(img_array)
                self.process_text(text)

    def close_audio_stream(self):
        self.audio_service.stop_audio()
        print("Audio stream closed")

