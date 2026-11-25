import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

print("===== Available Gemini Models =====")

for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)

print("Gemini API connection successful.")
