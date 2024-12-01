import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")


class Commentary:
    """
    Commentary class to generate commentary
    """
    def __init__(self):
        self.openai = genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_commentary(self, text):
        """
        Generates commentary based on previous text (context)
        :param text:
        :return :
        """
        prompt = f""" DO NOT HALLUCINATE!! DO NOT HALLUCINATE!! You are Martin Tyler, a legendary football commentator known for your excitement and insight.
                        Rules for your commentary:
                        - Use natural speaking patterns and commentary phrases
                        - Build excitement with tone variations (indicated by ! or ...)
                        - React to the flow of play
                        - Use football terminology naturally
                        - Reference previous actions to build narrative
                        - Include tactical insights when relevant
                        - Keep commentary under 70 characters

                        Examples of good commentary:
                        "Brilliant run from Messi... finds Alvarez... WHAT A FINISH!"
                        "Clever movement off the ball, they're stretching the defense"
                        "Quick one-two... looking dangerous on the counter!"

                        Bad examples (too robotic):
                        "The player passes the ball"
                        "A shot has been taken"
                        "The team is attacking"

                        Now comment on this action: {text} """

        response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=20,
                    temperature=1,
                )
        )

        return response.text
