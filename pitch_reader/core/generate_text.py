# # from google import genai
# # from google.genai import types
# # import requests
# # import json
# from groq import Groq
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# api_key = os.environ.get("GROQ_API_KEY")
#
#
#
#
# class Commentary:
#     """
#     Commentary class to generate commentary
#     """
#     def __init__(self):
#         # self.client = genai.Client()
#         api_key = os.environ.get("GROQ_API_KEY")
#         # self.base_url = "http://localhost:11434"
#         # self.model_name = "llama3"
#         self.model = "gemma2-9b-it"
#         self.client = Groq(api_key=api_key)
#
#     def generate_commentary(self, text):
#         """
#         Generates commentary based on previous text (context)
#
#         """
# #         prompt = f""" You are Martin Tyler commenting on this sequence of football actions: {text}
# #
# # Rules:
# # - Maximum 12 words total
# # - Create ONE commentary that tells the story of the sequence
# # - No player names unless given
# # - No team names
# # - No stage directions or parentheses
# # - Don't spam adjectives and superlatives
# # - Focus on the flow and outcome
# #
# # Examples (DO NOT SAY "SEUQUENCE":
# # Sequence: "pass → cross → shot → save" → "Good buildup but keeper denies them!"
# # Sequence: "tackle → pass → shot → goal" → "Wins it back and finishes brilliantly!"
# # Sequence: "corner → header → block → clearance" → "Close from the corner but cleared away!"
# # Single: "shot on goal" → "What a strike!"
# #
# # Commentary:"""
#
#         # response = self.client.models.generate_content_stream(
#         #         model="gemini-2.5-flash",
#         #         contents=prompt,
#         #         config=types.GenerateContentConfig(
#         #             thinking_config=types.ThinkingConfig(thinking_budget=0)
#         #         )
#
#         response = self.client.chat.completions.create(
#             model=self.model,
#             messages=[{
#                 "role": "system",
#                 "content": "You are a soccer commentator. Give 8 words of exciting commentary. No punctuation. No extra words. Do not hallucinate"
#             }, {
#                 "role": "user",
#                 "content": f"Action: {text}"
#             }],
#             max_tokens=16,
#             temperature=0.1,  # Low for consistency
#             top_p=0.3,
#             frequency_penalty=1.0,
#             presence_penalty=1.0,
#             stop=["\n", ".", "!"]
#         )
#
#         commentary = response.choices[0].message.content.strip()
#
#         # response = requests.post(
#         #     f"{self.base_url}/api/generate",
#         #     json={
#         #         "model": self.model_name,
#         #         "prompt": prompt,
#         #         "stream": True,
#         #         "options": {
#         #             "temperature": 0.0,
#         #             "top_p": 0.1,
#         #             "num_predict": 30,
#         #             "repeat_penalty": 1.0,
#         #         }
#         #      },
#         #     timeout = 30,
#         #     stream=True
#         # )
#         #
#         # if response.status_code == 200:
#         #     full_response = ""
#         #
#         #     # steaming response
#         #     for line in response.iter_lines():
#         #         if line:
#         #             try:
#         #                 chunk = json.loads(line)
#         #                 token = chunk.get("response", "")
#         #                 full_response += token
#         #
#         #                 # Stop when done
#         #                 if chunk.get("done", False):
#         #                     break
#         #             except json.JSONDecodeError:
#         #                 continue
#         #     response = full_response.strip()
#
#         return commentary
