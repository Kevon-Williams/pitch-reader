class ScreenConfig:
    def __init__(self):
        self.top = 928
        self.left = 468
        self.width = 984
        self.height = 20

    def resolution(self):
        return {
            "top": self.top,
            "left": self.left,
            "width": self.width,
            "height": self.height
        }

class AudioConfig:
    def __init__(self):
        self.format = 8
        self.channels = 1
        self.rate = 24_000
