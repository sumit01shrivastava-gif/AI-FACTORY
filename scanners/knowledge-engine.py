from pathlib import Path

ROOT = Path.home() / "AI-FACTORY"

KNOWLEDGE_ROOT = ROOT / "knowledge"
REPOSITORY_ROOT = ROOT / "repositories"


def build_knowledge(project_name):

    repository = REPOSITORY_ROOT / project_name

    if not repository.exists():
        print("Repository not found.")
        return

    print(f"Analyzing {project_name}")

    files = []

    for path in repository.rglob("*"):

        if path.is_file():
            files.append(str(path))

    return {
        "project": project_name,
        "files": len(files),
    }


if __name__ == "__main__":

    project = input("Project: ").strip()

    result = build_knowledge(project)

    print(result)
