import os
import click
from dotenv import load_dotenv
from pitch_reader.core.reader import ScreenReader

@click.command()
@click.option("--duration", default=60, help="Enter duration in seconds")
def main(duration):
    """Football Manager commentary voice app."""
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")

    reader = ScreenReader(api_key)
    reader.take_screenshot_and_process(duration)


if __name__ == "__main__":
    main()