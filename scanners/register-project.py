import json
from pathlib import Path

ROOT = Path.home() / "AI-FACTORY"

REPOSITORY_ROOT = ROOT / "repositories"
REGISTRY_ROOT = ROOT / "registry"


project = input("Project name: ").strip().lower()
category = input("Category: ").strip().lower()

repository_path = REPOSITORY_ROOT / project

if not repository_path.exists():
    raise ValueError("Repository does not exist.")

project_path = REGISTRY_ROOT / category / project

project_path.mkdir(parents=True, exist_ok=True)

manifest = {
    "name": project,
    "category": category,
    "repository": str(repository_path),
    "status": "active",
    "agents": [],
    "tags": [],
}

manifest_file = project_path / "manifest.json"

with open(manifest_file, "w") as file:
    json.dump(manifest, file, indent=4)

print(f"{project} registered successfully.")
