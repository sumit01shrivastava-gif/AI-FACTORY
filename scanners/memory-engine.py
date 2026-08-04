import json
from pathlib import Path

ROOT = Path.home() / "AI-FACTORY"

MEMORY_ROOT = ROOT / "memory"


def create_memory(project):

    data = {
        "project": project,
        "tasks": [],
        "decisions": [],
        "knowledge": [],
        "history": [],
        "deployments": [],
        "errors": []
    }

    path = MEMORY_ROOT / f"{project}.json"

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

    print("Memory initialized.")
