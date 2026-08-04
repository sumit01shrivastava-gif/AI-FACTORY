from agents.architect.architect import Architect
from agents.backend.backend import BackendAgent
from agents.deployment.deployment import DeploymentAgent
from agents.frontend.frontend import FrontendAgent
from agents.planner.planner import Planner
from agents.qa.qa import QAAgent
from agents.research.research import ResearchAgent


class AgentRegistry:

    def __init__(self):

        self.agents = {
            "planner": Planner(),
            "research": ResearchAgent(),
            "architect": Architect(),
            "backend": BackendAgent(),
            "frontend": FrontendAgent(),
            "qa": QAAgent(),
            "deployment": DeploymentAgent(),
        }

    def get(self, name):
        return self.agents.get(name)

    def list(self):
        return list(self.agents.keys())
