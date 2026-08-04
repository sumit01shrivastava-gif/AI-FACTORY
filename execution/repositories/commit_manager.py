import subprocess


class CommitManager:

    def commit(self, repository, message):

        subprocess.run(
            ["git", "add", "."],
            cwd=repository,
        )

        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=repository,
        )

        return True
