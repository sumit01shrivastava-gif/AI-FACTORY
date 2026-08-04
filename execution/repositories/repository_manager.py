from pathlib import Path


class RepositoryManager:

    ROOT = Path("repositories")

    def list(self):
        return [
            x.name
            for x in self.ROOT.iterdir()
            if x.is_dir()
        ]
