# from openai import OpenAI
# import pyaudio
#
# class TTS:
#     def __init__(self, api_key):
#         self.openai = OpenAI(api_key=api_key)
#
#     def text_to_speech(self, text):
#         with self.openai.audio.speech.with_streaming_response.create(
#                 model="tts-1",
#                 voice="nova",
#                 input=text,
#                 response_format="pcm"
#         ) as response:
#             for chunk in response.iter_bytes(1024):
#                 stream.write(chunk)
