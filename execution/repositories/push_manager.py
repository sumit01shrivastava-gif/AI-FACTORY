import subprocess


class PushManager:

    def push(self, repository):

        subprocess.run(
            ["git", "push"],
            cwd=repository,
        )

        return True
