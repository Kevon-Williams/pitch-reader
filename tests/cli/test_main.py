import unittest
from unittest.mock import patch, Mock
from pitch_reader.cli.main import Main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.duration = 5
        self.main = Main(self.duration)

    def test_initialization(self):
        self.assertEqual(self.main.duration, self.duration)

    @patch('pitch_reader.cli.main.ScreenReader')
    def test_main_execution(self, mock_screen_reader):
        mock_reader = mock_screen_reader.return_value


        self.main.main()

        mock_screen_reader.assert_called_once()
        mock_reader.start.assert_called_once_with(self.duration)


if __name__ == '__main__':
    unittest.main()
