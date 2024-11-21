import pyaudio
from pitch_reader.core.config import AudioConfig

class Audio:
    def __init__(self):
        self.config = AudioConfig()
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_audio_stream(self):
        self.stream = self.audio.open(
            format=self.config.format,
            channels=self.config.channels,
            rate=self.config.rate,
            output=True
        )

    def write_chunk(self, chunks):
        if self.stream:
            self.stream.write(chunks)

    def stop_audio(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()

