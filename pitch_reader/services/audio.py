import pyaudio
from openai import OpenAI
from pitch_reader.core.config import AudioConfig
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

class Audio:
    """
    Audio class to play audio from text
    """
    def __init__(self):
        self.config = AudioConfig()
        self.openai = OpenAI(api_key=api_key)
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_audio_stream(self, text):
        """
        Starts the audio stream (plays the audio)
        :param text:
        :return:
        """
        self.stream = self.audio.open(
            format=self.config.format,
            channels=self.config.channels,
            rate=self.config.rate,
            output=True
        )

        with self.openai.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice="alloy",
                input=text,
                response_format="pcm"
        ) as response:
            for chunk in response.iter_bytes(1024):
                self.stream.write(chunk)



    def stop_audio(self):
        """
        Stops the audio stream (stops audio)
        :return:
        """
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()

