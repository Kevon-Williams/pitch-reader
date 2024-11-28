import unittest
from pitch_reader.core.generate_text import Commentary

class TestGenerateText(unittest.TestCase):
    def setUp(self):
        self.commentary = Commentary()
        self.previous_texts = """Ojeda recieves a tidy pass", "Ojeda takes a shot on goal", "Ojeda scores a goal"""

    def test_generate_commentary(self):
        result = self.commentary.generate_commentary(text=self.previous_texts)

        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        print(f"Generated commentary: {result}")

if __name__ == '__main__':
    unittest.main()