import subprocess


class PytestValidator:

    def validate(
        self,
        directory="tests",
    ):

        result = subprocess.run(
            [
                "pytest",
                directory,
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
