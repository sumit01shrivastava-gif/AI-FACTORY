from pathlib import Path


class RepositoryEditor:

    def read(self, filename):

        path = Path(filename)

        return path.read_text()

    def write(self, filename, content):

        path = Path(filename)

        path.write_text(content)

    def append(self, filename, content):

        path = Path(filename)

        existing = path.read_text()

        path.write_text(
            existing + "\n" + content
        )
