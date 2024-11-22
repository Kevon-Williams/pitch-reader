from openai import OpenAI

class Commentary:
    def __init__(self, api_key):
        self.openai = OpenAI(api_key=api_key)

    def generate_commentary(self, previous_texts):

        response = self.openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": """ Act as a concise football commentator. Focus on:
                    - Tactical insights
                    - Play-by-play action
                    - Player movements and decisions
                    Keep commentary under 50 characters.
                    Make it flow naturally with previous comments."""},
                {"role": "user", "content": previous_texts}
            ],
            max_tokens=15,
            temperature=0.7,
            presence_penalty=0.3
        )

        return response.choices[0].message.content
