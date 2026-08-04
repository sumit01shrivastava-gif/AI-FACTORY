class Planner:

    def execute(self):
        return {
            "project": "shopify-video-ai",
            "description": "Build an AI-powered Shopify video generator.",
            "steps": [
                "Analyze requirements",
                "Research competitors",
                "Create architecture",
                "Build backend",
                "Build frontend",
                "Run tests",
                "Deploy",
            ],
        }


if __name__ == "__main__":
    planner = Planner()
    print(planner.execute())
