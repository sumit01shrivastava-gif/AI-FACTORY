from agents.team.planner_agent import (
    PlannerAgent,
)
from agents.team.research_agent import (
    ResearchAgent,
)
from agents.team.architect_agent import (
    ArchitectAgent,
)
from agents.team.backend_agent import (
    BackendAgent,
)
from agents.team.frontend_agent import (
    FrontendAgent,
)
from agents.team.qa_agent import (
    QAAgent,
)
from agents.team.deployment_agent import (
    DeploymentAgent,
)


class TeamManager:

    def __init__(self):

        self.agents = [
            PlannerAgent(),
            ResearchAgent(),
            ArchitectAgent(),
            BackendAgent(),
            FrontendAgent(),
            QAAgent(),
            DeploymentAgent(),
        ]

    def execute(
        self,
        task,
    ):

        results = []

        for agent in self.agents:

            results.append(
                agent.execute(
                    task
                )
            )

        return results
