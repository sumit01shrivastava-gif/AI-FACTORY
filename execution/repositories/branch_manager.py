import subprocess


class BranchManager:

    def create(self, repository, branch):

        subprocess.run(
            ["git", "checkout", "-b", branch],
            cwd=repository,
        )
