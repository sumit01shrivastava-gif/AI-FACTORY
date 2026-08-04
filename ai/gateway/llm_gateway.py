from ai.gateway.provider_registry import (
    ProviderRegistry,
)


class LLMGateway:

    def __init__(self):

        self.registry = (
            ProviderRegistry()
        )

    def register_provider(
        self,
        name,
        provider,
    ):

        self.registry.register(
            name,
            provider,
        )

    def generate(
        self,
        provider_name,
        prompt,
    ):

        provider = self.registry.get(
            provider_name
        )

        if provider is None:

            raise ValueError(
                "Unknown provider"
            )

        return provider.generate(
            prompt
        )
