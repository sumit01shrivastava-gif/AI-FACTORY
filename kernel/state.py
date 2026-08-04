import json
from pathlib import Path

ROOT = Path.home() / "AI-FACTORY"

STATE_ROOT = ROOT / "runtime" / "state"


class StateManager:

    def save(self, name, data):

        STATE_ROOT.mkdir(parents=True, exist_ok=True)

        file_path = STATE_ROOT / f"{name}.json"

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self, name):

        file_path = STATE_ROOT / f"{name}.json"

        if not file_path.exists():
            return None

        with open(file_path) as file:
            return json.load(file)


if __name__ == "__main__":

    manager = StateManager()

    manager.save(
        "system",
        {
            "status": "running",
            "projects": [
                "terrax",
                "xentra"
            ]
        }
    )

    print(manager.load("system"))
