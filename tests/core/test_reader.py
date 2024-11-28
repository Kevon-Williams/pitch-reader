import unittest
from collections import deque
from pitch_reader.core.reader import ScreenReader

class TestScreenReader(unittest.TestCase):
    def setUp(self):
        self.screen_reader = ScreenReader()

    def test_screen_reader_initialization(self):
        self.assertIsInstance(self.screen_reader.previous_texts, deque)
        self.assertEqual(self.screen_reader.previous_texts.maxlen, 10)
        self.assertTrue(hasattr(self.screen_reader, 'screen_config'))
        self.assertTrue(hasattr(self.screen_reader, 'commentary'))
        self.assertTrue(hasattr(self.screen_reader, 'audio_service'))
        self.assertTrue(hasattr(self.screen_reader, 'ocr'))

if __name__ == "__main__":
    unittest.main()
