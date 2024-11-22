import easyocr

class Ocr:
    """
    Ocr class to process image and extract text
    """
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=True)

    def process_image(self, image):
        """
        Process the image and extract text
        :param image:
        :return text from image:
        """
        results = self.reader.readtext(image)
        return "".join(result[1] for result in results)
