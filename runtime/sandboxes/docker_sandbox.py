import subprocess
from pathlib import Path


class DockerSandbox:

    def __init__(self, image="python:3.12"):
        self.image = image

    def execute(self, directory):

        directory = Path(directory).resolve()

        result = subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{directory}:/workspace",
                "-w",
                "/workspace",
                self.image,
                "python",
                "main.py",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
