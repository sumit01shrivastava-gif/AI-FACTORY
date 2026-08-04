from pathlib import Path


class Workspace:

    ROOT = Path("repositories")

    def get(self, project):
        return self.ROOT / project

    def exists(self, project):
        return self.get(project).exists()


if __name__ == "__main__":
    workspace = Workspace()

    print(workspace.get("terrax"))
