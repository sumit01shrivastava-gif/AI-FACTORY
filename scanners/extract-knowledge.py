import json
from pathlib import Path

ROOT = Path.home() / "AI-FACTORY" / "repositories"

for repository in ROOT.iterdir():
    if not repository.is_dir():
        continue

    print("\n" + "=" * 60)
    print(repository.name.upper())
    print("=" * 60)

    package_json = repository / "package.json"

    if package_json.exists():
        data = json.loads(package_json.read_text())

        print("\nProject name:")
        print(data.get("name"))

        print("\nDependencies:")

        dependencies = data.get("dependencies", {})

        for dependency in sorted(dependencies.keys()):
            print("-", dependency)

    readme = repository / "README.md"

    if readme.exists():
        print("\nREADME found.")
