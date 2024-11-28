from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")


class Commentary:
    """
    Commentary class to generate commentary
    """
    def __init__(self):
        self.openai = OpenAI(api_key=api_key)

    def generate_commentary(self, previous_texts):
        """
        Generates commentary based on previous texts (context)
        :param previous_texts:
        :return :
        """
        response = self.openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": """ You are Martin Tyler, a legendary football commentator known for your excitement and insight.
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
                    "The team is attacking"""},
                {"role": "user", "content": previous_texts}
            ],
            max_tokens=20,
            temperature=0.5
        )

        return response.choices[0].message.content
