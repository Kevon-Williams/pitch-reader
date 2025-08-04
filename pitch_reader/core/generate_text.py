from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")




class Commentary:
    """
    generates commentary from text using Groq API
    """
    def __init__(self):
        self.model = "gemma2-9b-it"
        self.client = Groq(api_key=api_key)

    def generate_commentary(self, text):
        """
        generates commentary from the text using Groq API
        :param text:
        :return commentary:
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{
                "role": "system",
                "content": """You are a soccer commentator. Comment based on the input. Add function words (articles auxiliary verbs,
        #                      prepositions, conjunctions) when needed."""
            }, {
                "role": "user",
                "content": f"Action: {text}"
            }],
            max_tokens=20,
            temperature=0.1,
            top_p=0.3,
            frequency_penalty=1.0,
            presence_penalty=1.0,
            stop=["\n", ".", "!"],
        )

        commentary = response.choices[0].message.content.strip()

        return commentary
