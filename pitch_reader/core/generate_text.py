from openai import OpenAI

class Commentary:
    def __init__(self, api_key):
        self.openai = OpenAI(api_key=api_key)

    def generate_commentary(self, previous_texts):

        response = self.openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "Act as a concise football commentator. Comment intelligently with a focus on play-by-play and tactics. Max 70 characters."},
                {"role": "user", "content": previous_texts}
            ],
            max_tokens=20
        )

        return response.choices[0].message.content
