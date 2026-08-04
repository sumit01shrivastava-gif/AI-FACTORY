import subprocess


class GitManager:

    def status(self, repository):
        result = subprocess.run(
            ["git", "status"],
            cwd=repository,
            capture_output=True,
            text=True,
        )

        return result.stdout
