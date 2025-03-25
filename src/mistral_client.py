from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os
from dotenv import load_dotenv

# Load .env file only as a fallback
load_dotenv(override=False)  # This ensures system environment variables take precedence

class MistralHandler:
    def __init__(self):
        # First try to get from system environment, then fallback to .env if needed
        api_key = os.environ.get('MISTRAL_API_KEY')
        if not api_key:
            raise ValueError("MISTRAL_API_KEY environment variable is not set in system environment")
        self.client = MistralClient(api_key=api_key)
        self.model = "mistral-tiny"  # You can change this to other models like "mistral-small" or "mistral-medium"

    def get_response(self, user_message: str) -> str:
        try:
            messages = [
                ChatMessage(role="user", content=user_message)
            ]
            
            chat_response = self.client.chat(
                model=self.model,
                messages=messages
            )
            
            return chat_response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}" 