import unittest
from pitch_reader.services.audio import Audio

class TestAudio(unittest.TestCase):
    def setUp(self):
        self.audio = Audio()

    def test_start_audio_stream(self):
        text = "What an Incredible goal!"
        self.audio.start_audio_stream(text)
        self.assertTrue(self.audio.stream)

    def test_stop_audio(self):
        self.audio.stop_audio()
        self.assertFalse(self.audio.stream)

if __name__ == "__main__":
    unittest.main()