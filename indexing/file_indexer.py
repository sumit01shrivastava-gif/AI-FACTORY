from pathlib import Path


class FileIndexer:

    def index(
        self,
        directory=".",
    ):

        root = Path(directory)

        return [
            str(path)
            for path in root.rglob("*")
            if path.is_file()
        ]
