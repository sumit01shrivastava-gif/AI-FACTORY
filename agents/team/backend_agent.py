from agents.core.base_agent import (
    BaseAgent,
)


class BackendAgent(
    BaseAgent,
):

    def __init__(self):

        super().__init__(
            "backend"
        )

    def execute(
        self,
        task,
    ):

        return {
            "agent": self.name,
            "task": task,
        }
