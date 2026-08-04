from providers.ai.claude import ClaudeProvider
from providers.ai.openai_provider import OpenAIProvider


class AIProviderFactory:

    @staticmethod
    def create(provider="openai"):

        providers = {
            "openai": OpenAIProvider,
            "claude": ClaudeProvider,
        }

        if provider not in providers:
            raise ValueError(
                f"Unknown provider: {provider}"
            )

        return providers[provider]()
