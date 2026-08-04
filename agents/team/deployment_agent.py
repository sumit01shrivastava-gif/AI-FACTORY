from agents.core.base_agent import (
    BaseAgent,
)


class DeploymentAgent(
    BaseAgent,
):

    def __init__(self):

        super().__init__(
            "deployment"
        )

    def execute(
        self,
        task,
    ):

        return {
            "agent": self.name,
            "task": task,
        }
