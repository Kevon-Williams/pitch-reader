import unittest
from pitch_reader.core.config import ScreenConfig, AudioConfig

class TestScreenConfig(unittest.TestCase):
    def setUp(self):
        self.screen_config = ScreenConfig()

    def test_default_values(self):
        self.assertEqual(self.screen_config.top, 928)
        self.assertEqual(self.screen_config.left, 468)
        self.assertEqual(self.screen_config.width, 984)
        self.assertEqual(self.screen_config.height, 20)

    def test_resolution_returns_correct_dict(self):
        expected = {
            "top": 928,
            "left": 468,
            "width": 984,
            "height": 20
        }

        self.assertEqual(self.screen_config.resolution(), expected)

class TestAudioConfig(unittest.TestCase):
    def setUp(self):
        self.audio_config = AudioConfig()

    def test_default_values(self):
        self.assertEqual(self.audio_config.format, 8)
        self.assertEqual(self.audio_config.channels, 1)
        self.assertEqual(self.audio_config.rate, 24_000)

if __name__ == '__main__' :
    unittest.main()
