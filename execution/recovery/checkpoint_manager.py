import shutil
from pathlib import Path


class CheckpointManager:

    def create(self, source, destination):

        source = Path(source)

        destination = Path(destination)

        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True,
        )
