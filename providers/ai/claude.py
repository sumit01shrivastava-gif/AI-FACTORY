import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class ClaudeProvider:

    def __init__(self):
        self.client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

    def execute(self, prompt):

        response = self.client.messages.create(
            model="claude-sonnet-4-0",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.content[0].text
