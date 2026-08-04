import subprocess


class RuffValidator:

    def validate(self, directory="."):

        result = subprocess.run(
    ["ruff", "check", directory],
    capture_output=True,
    text=True,
    check=False,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
