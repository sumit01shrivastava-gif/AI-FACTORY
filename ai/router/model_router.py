from ai.providers.openai_provider import (
    OpenAIProvider,
)
from ai.providers.anthropic_provider import (
    AnthropicProvider,
)


class ModelRouter:

    def __init__(self):

        self.providers = {
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider(),
        }

    def route(
        self,
        provider,
        prompt,
    ):

        return self.providers[
            provider
        ].generate(
            prompt,
        )
