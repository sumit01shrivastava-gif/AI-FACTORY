import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class OpenAIProvider:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def execute(self, prompt):

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt,
        )

        return response.output_text
