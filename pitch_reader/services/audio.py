import pyaudio
from openai import OpenAI
from pitch_reader.core.config import AudioConfig

class Audio:
    def __init__(self, api_key):
        self.config = AudioConfig()
        self.openai = OpenAI(api_key=api_key)
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_audio_stream(self, text):
        self.stream = self.audio.open(
            format=self.config.format,
            channels=self.config.channels,
            rate=self.config.rate,
            output=True
        )

        with self.openai.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice="echo",
                input=text,
                response_format="pcm"
        ) as response:
            for chunk in response.iter_bytes(1024):
                self.stream.write(chunk)



    def stop_audio(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()

