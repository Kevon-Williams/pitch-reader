import easyocr

class Ocr:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=True)

    def process_image(self, image):
        results = self.reader.readtext(image)
        return "".join(result[1] for result in results)
