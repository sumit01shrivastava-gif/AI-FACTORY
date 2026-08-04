from scanners.orchestrator import Orchestrator


def main():

    orchestrator = Orchestrator()

    result = orchestrator.execute(
        "shopify-video-ai",
        "Build an AI-powered Shopify video generator."
    )

    print(result)


if __name__ == "__main__":
    main()
