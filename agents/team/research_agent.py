from agents.core.base_agent import (
    BaseAgent,
)


class ResearchAgent(
    BaseAgent,
):

    def __init__(self):

        super().__init__(
            "research"
        )

    def execute(
        self,
        task,
    ):

        return {
            "agent": self.name,
            "task": task,
        }
