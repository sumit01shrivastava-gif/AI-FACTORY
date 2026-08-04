from pathlib import Path

ROOT = Path.home() / "AI-FACTORY"

REGISTRY_ROOT = ROOT / "registry"

CATEGORIES = [
    "active",
    "incubation",
    "experimental",
    "archived",
]


class ProjectRegistry:

    def __init__(self):
        self.projects = []

    def load_projects(self):

        self.projects = []

        for category in CATEGORIES:

            category_path = REGISTRY_ROOT / category

            if not category_path.exists():
                continue

            for project in category_path.iterdir():

                if project.is_dir():

                    self.projects.append(
                        {
                            "name": project.name,
                            "category": category,
                            "path": str(project),
                        }
                    )

        return self.projects

    def get_project(self, name):

        for project in self.projects:

            if project["name"] == name:
                return project

        return None


if __name__ == "__main__":

    registry = ProjectRegistry()

    projects = registry.load_projects()

    print("\nPROJECTS\n")

    for project in projects:
        print(project)
