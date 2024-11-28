import unittest
from pitch_reader.services.ocr import Ocr

class TestOcr(unittest.TestCase):
    def setUp(self):
        self.ocr = Ocr()

    def test_process_image(self):
        image = "ocr_test_img/img.png"
        text = self.ocr.process_image(image)
        self.assertEqual(text, "Thank you")

if __name__ == '__main__':
    unittest.main()