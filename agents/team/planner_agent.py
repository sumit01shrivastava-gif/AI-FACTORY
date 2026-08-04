from agents.core.base_agent import (
    BaseAgent,
)


class PlannerAgent(
    BaseAgent,
):

    def __init__(self):

        super().__init__(
            "planner"
        )

    def execute(
        self,
        task,
    ):

        return {
            "agent": self.name,
            "task": task,
        }
