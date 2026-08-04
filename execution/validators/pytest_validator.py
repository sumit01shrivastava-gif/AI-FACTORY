import subprocess


class PytestValidator:

    def validate(self):

        result = subprocess.run(
    ["pytest"],
    capture_output=True,
    text=True,
    check=False,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
