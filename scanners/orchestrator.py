from agents.architect.architect import Architect
from agents.backend.backend import BackendAgent
from agents.deployment.deployment import DeploymentAgent
from agents.frontend.frontend import FrontendAgent
from agents.planner.planner import Planner
from agents.qa.qa import QAAgent
from agents.research.research import ResearchAgent


class Orchestrator:

    def run(self):

        planner = Planner()
        researcher = ResearchAgent()
        architect = Architect()
        backend = BackendAgent()
        frontend = FrontendAgent()
        qa = QAAgent()
        deployment = DeploymentAgent()

        plan = planner.execute()

        research = researcher.execute(plan)

        architecture = architect.execute(research)

        backend.execute(architecture)

        frontend.execute(architecture)

        qa.execute()

        deployment.execute()

        print("Project completed.")
