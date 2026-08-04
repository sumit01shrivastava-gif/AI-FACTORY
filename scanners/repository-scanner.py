import os
from pathlib import Path

EXCLUDED = {
    ".git",
    "node_modules",
    ".next",
    "dist",
    "build",
    ".vercel",
    ".turbo",
    ".cursor",
}

ROOT = Path.home() / "AI-FACTORY" / "repositories"


def scan_repository(repo_path):
    result = {
        "files": [],
        "directories": [],
    }

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDED]

        for directory in dirs:
            result["directories"].append(
                str(Path(root) / directory)
            )

        for file in files:
            result["files"].append(
                str(Path(root) / file)
            )

    return result


for repository in ROOT.iterdir():
    if repository.is_dir():
        data = scan_repository(repository)

        print("\n")
        print("=" * 60)
        print(repository.name.upper())
        print("=" * 60)
        print(f"Directories: {len(data['directories'])}")
        print(f"Files: {len(data['files'])}")
