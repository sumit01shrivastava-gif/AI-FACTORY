from pathlib import Path


class FileTool:

    def read(
        self,
        path,
    ):

        return Path(path).read_text()

    def write(
        self,
        path,
        content,
    ):

        Path(path).write_text(
            content,
        )
