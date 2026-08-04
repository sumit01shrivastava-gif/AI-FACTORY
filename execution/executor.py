from execution.prompt_builder import PromptBuilder
from providers.ai.factory import AIProviderFactory


class Executor:

    def __init__(self, provider="openai"):

        self.ai = AIProviderFactory.create(
            provider
        )

        self.builder = PromptBuilder()

    def execute(
        self,
        project,
        task,
        architecture,
    ):

        prompt = self.builder.build(
            project,
            task,
            architecture,
        )

        return self.ai.execute(prompt)
