from ai.providers.base_provider import (
    BaseProvider,
)


class AnthropicProvider(
    BaseProvider,
):

    def __init__(self):

        self.model = "claude"

    def generate(
        self,
        prompt,
    ):

        return {
            "provider": "anthropic",
            "response": prompt,
        }
