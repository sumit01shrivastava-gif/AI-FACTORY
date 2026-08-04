from agents.core.base_agent import (
    BaseAgent,
)


class FrontendAgent(
    BaseAgent,
):

    def __init__(self):

        super().__init__(
            "frontend"
        )

    def execute(
        self,
        task,
    ):

        return {
            "agent": self.name,
            "task": task,
        }
