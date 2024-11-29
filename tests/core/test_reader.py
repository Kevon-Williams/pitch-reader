import unittest
from collections import deque
from queue import Queue
from pitch_reader.core.reader import ScreenReader

class TestScreenReader(unittest.TestCase):
    def setUp(self):
        self.screen_reader = ScreenReader()

    def test_screen_reader_initialization(self):

        self.assertIsInstance(self.screen_reader.previous_texts, deque)
        self.assertEqual(self.screen_reader.previous_texts.maxlen, 10)

        # Test queue data
        queues = [
            self.screen_reader.image_queue,
            self.screen_reader.text_queue,
            self.screen_reader.commentary_queue
        ]
        for queue in queues:
            self.assertIsInstance(queue, Queue)
            self.assertEqual(queue.maxsize, 5)

        # Test threads
        self.assertFalse(self.screen_reader.running)
        self.assertEqual(self.screen_reader.threads, [])

        # Test rservices
        required_attrs = ['screen_config', 'commentary', 'audio_service', 'ocr', 'executor']
        for attr in required_attrs:
            self.assertTrue(hasattr(self.screen_reader, attr))

if __name__ == "__main__":
    unittest.main()
