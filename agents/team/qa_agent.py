from agents.core.base_agent import (
    BaseAgent,
)


class QAAgent(
    BaseAgent,
):

    def __init__(self):

        super().__init__(
            "qa"
        )

    def execute(
        self,
        task,
    ):

        return {
            "agent": self.name,
            "task": task,
        }
