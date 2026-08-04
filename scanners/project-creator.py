from pathlib import Path

ROOT = Path.home() / "AI-FACTORY"

VALID_CATEGORIES = [
    "active",
    "incubation",
    "experimental",
    "archived"
]

project_name = input("Project name: ").strip().lower()

category = input(
    "Category (active/incubation/experimental/archived): "
).strip().lower()

if category not in VALID_CATEGORIES:
    raise ValueError(
        f"Invalid category. Choose one of {VALID_CATEGORIES}"
    )

registry_path = ROOT / "registry" / category / project_name
knowledge_path = ROOT / "knowledge" / category / project_name
repository_path = ROOT / "repositories" / project_name

registry_path.mkdir(parents=True, exist_ok=True)
knowledge_path.mkdir(parents=True, exist_ok=True)
repository_path.mkdir(parents=True, exist_ok=True)

print("\nProject created successfully.")
print(f"Registry: {registry_path}")
print(f"Knowledge: {knowledge_path}")
print(f"Repository: {repository_path}")
