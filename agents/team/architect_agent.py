from agents.core.base_agent import (
    BaseAgent,
)


class ArchitectAgent(
    BaseAgent,
):

    def __init__(self):

        super().__init__(
            "architect"
        )

    def execute(
        self,
        task,
    ):

        return {
            "agent": self.name,
            "task": task,
        }
