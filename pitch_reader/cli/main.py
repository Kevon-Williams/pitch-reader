from pitch_reader.core.reader import ScreenReader

class Main:
    """
    Main class to start the program
    :param duration: int: duration in seconds to run the program
    """
    def __init__(self, duration=300, sleep_time=5):
        self.duration = duration
        self.sleep_time = sleep_time

    def main(self):
        """
        Main function to start the program
        """
        reader = ScreenReader()
        reader.take_screenshot_and_process(self.duration, self.sleep_time)
        reader.close_audio_stream()


if __name__ == "__main__":
    Main(300, 5).main()
