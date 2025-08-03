from pitch_reader.core.reader import ScreenReader

class Main:
    """
    Main class to start the program
    :param duration: int: duration in seconds to run the program
    """
    def __init__(self, duration=300):
        self.duration = duration

    def main(self):

        reader = ScreenReader()
        reader.start(self.duration)


if __name__ == "__main__":
    Main(300).main()
