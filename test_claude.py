from providers.ai.claude import ClaudeProvider

provider = ClaudeProvider()

response = provider.execute(
    "Explain the repository pattern in Python."
)

print(response)
