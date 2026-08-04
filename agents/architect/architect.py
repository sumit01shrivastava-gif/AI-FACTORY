class Architect:

    def execute(self, research):
        return {
            "frontend": "Next.js",
            "backend": "FastAPI",
            "database": "PostgreSQL",
        }


if __name__ == "__main__":
    architect = Architect()

    print(
        architect.execute(
            {"project": "demo"}
        )
    )
