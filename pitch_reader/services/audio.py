from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")



class Audio:
    """
    Audio class to play audio from text
    """
    def __init__(self):
        self.elevenlabs = ElevenLabs (
            api_key = os.environ.get("ELEVENLABS_API_KEY"),
        )

    def start_audio_stream(self, text):
        """
        starts the audio stream
        :param text:
        :return:
        """

        audio = self.elevenlabs.text_to_speech.convert(
            text=text,
            voice_id="bVM5MBBFUy5Uve0cooHn",
            model_id="eleven_flash_v2_5",
            output_format="mp3_44100_128"
        )

        stream(audio)


