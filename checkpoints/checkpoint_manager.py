from pathlib import Path
import json


class CheckpointManager:

    def __init__(
        self,
        path="checkpoints",
    ):
        self.path = Path(path)

        self.path.mkdir(
            exist_ok=True,
        )

    def save(
        self,
        name,
        data,
    ):
        file_path = self.path / f"{name}.json"

        with open(
            file_path,
            "w",
        ) as file:
            json.dump(
                data,
                file,
                indent=2,
            )

    def load(
        self,
        name,
    ):
        file_path = self.path / f"{name}.json"

        if not file_path.exists():
            return None

        with open(file_path) as file:
            return json.load(file)
