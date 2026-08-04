from ai.providers.base_provider import (
    BaseProvider,
)


class OpenAIProvider(
    BaseProvider,
):

    def __init__(self):

        self.model = "gpt"

    def generate(
        self,
        prompt,
    ):

        return {
            "provider": "openai",
            "response": prompt,
        }
