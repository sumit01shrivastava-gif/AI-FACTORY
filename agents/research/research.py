class ResearchAgent:

    def execute(self, plan):
        return {
            "project": plan["project"],
            "technologies": [],
            "competitors": [],
        }


if __name__ == "__main__":
    agent = ResearchAgent()

    sample_plan = {
        "project": "demo"
    }

    print(agent.execute(sample_plan))
