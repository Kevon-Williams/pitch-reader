from openai import OpenAI

class Commentary:
    def __init__(self, api_key):
        self.openai = OpenAI(api_key=api_key)

    def generate_commentary(self, previous_texts):

        response = self.openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "I want you to act as a football commentator. I will give you descriptions of football matches in progress and you will commentate on the match. You should be knowledgeable of football terminology, tactics and focus primarily on providing intelligent commentary and narrating play-by-play. "},
                {"role": "user", "content": previous_texts}
            ],
            max_tokens=50
        )

        return response.choice[0].message
