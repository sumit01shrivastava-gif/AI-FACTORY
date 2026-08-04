import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

print("Loaded:", api_key[:20] + "...")

client = Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-sonnet-4-0",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Say hello."
        }
    ]
)

print(response.content[0].text)
