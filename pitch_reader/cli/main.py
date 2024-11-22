import os
from dotenv import load_dotenv
from pitch_reader.core.reader import ScreenReader

def main(duration):
    """
    Main function to start the program
    :param duration: int: duration in seconds to run the program
    """
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")

    reader = ScreenReader(api_key)
    reader.take_screenshot_and_process(duration, 5)
    reader.close_audio_stream()


if __name__ == "__main__":
    main(300)