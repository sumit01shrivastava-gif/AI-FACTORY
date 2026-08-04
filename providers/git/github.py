import subprocess


class GitProvider:

    def status(self):

        result = subprocess.run(
    ["git", "status"],
    capture_output=True,
    text=True,
    check=False,
        )

        return result.stdout


if __name__ == "__main__":

    git = GitProvider()

    print(git.status())
