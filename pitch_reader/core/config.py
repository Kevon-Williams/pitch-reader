class ScreenConfig:
    """
    ScreenConfig class to set the resolution of the screen
    """
    def __init__(self):
        self.top = 928
        self.left = 468
        self.width = 984
        self.height = 20

    def resolution(self):
        """
        Returns the resolution of the screen
        :return:
        """
        return {
            "top": self.top,
            "left": self.left,
            "width": self.width,
            "height": self.height
        }

class AudioConfig:
    """
    AudioConfig class to set the audio configuration
    """
    def __init__(self):
        self.format = 8
        self.channels = 1
        self.rate = 24_000
