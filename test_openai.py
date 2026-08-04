from providers.ai.openai_provider import OpenAIProvider

provider = OpenAIProvider()

response = provider.execute(
    "Explain the repository pattern in Python."
)

print(response)
