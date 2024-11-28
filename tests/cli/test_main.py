import unittest
from unittest.mock import patch, Mock
from pitch_reader.cli.main import Main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main(5, 5)


    def test_initialization(self):
        self.assertEqual(self.main.duration, 5, "Duration should be 5")
        self.assertEqual(self.main.sleep_time, 5, "sleep_time should be 5")

    @patch('pitch_reader.cli.main.ScreenReader')
    def test_main(self, mock_screen_reader):
        mock_reader_instance = mock_screen_reader.return_value

        main_instance = Main(duration=5, sleep_time=5)
        main_instance.main()


        mock_reader_instance.take_screenshot_and_process.assert_called_once_with(5, 5)
        mock_reader_instance.close_audio_stream.assert_called_once()


if __name__ == '__main__':
    unittest.main()
