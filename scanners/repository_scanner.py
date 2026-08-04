from pathlib import Path


class RepositoryScanner:

    def scan(self, repository):

        repository = Path(repository)

        files = []

        for file in repository.rglob("*"):

            if file.is_file():
                files.append(str(file))

        return files
