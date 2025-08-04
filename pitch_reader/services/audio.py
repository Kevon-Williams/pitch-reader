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

        self.stream = self.audio.open(
            format=self.config.format,
            channels=self.config.channels,
            rate=self.config.rate,
            output=True,
            frames_per_buffer=4096,
            start=True,
        )



    def start_audio_stream(self, text):
        """
        starts the audio stream
        :param text:
        :return:
        """

        with self.openai.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts",
                voice="fable",
                input=text,
                instructions="""You are a commentator. Repeat the input verbatim. Add function words (articles auxiliary verbs, 
                             prepositions, conjunctions) when needed. Do not add any extra words or phrases.""",
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

