from pathlib import Path


class GithubManager:

    def list_repository_files(
        self,
        directory=".",
    ):

        root = Path(directory)

        return [
            str(path)
            for path in root.rglob("*")
            if path.is_file()
        ]
