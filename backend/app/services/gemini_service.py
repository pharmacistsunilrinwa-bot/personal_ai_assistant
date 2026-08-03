import google.generativeai as genai
import os
import random
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_keys = os.getenv("GEMINI_API_KEYS", "").split(",")
        self.api_keys = [k.strip() for k in self.api_keys if k.strip()]
        if not self.api_keys:
            raise ValueError("No Gemini API keys found in environment variables.")
        
    def get_random_key(self):
        return random.choice(self.api_keys)

    async def generate_response(self, prompt: str, history: list = None):
        key = self.get_random_key()
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        chat = model.start_chat(history=history or [])
        response = chat.send_message(prompt)
        return response.text

gemini_service = GeminiService()
