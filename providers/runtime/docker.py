import subprocess


class DockerProvider:

    def ps(self):

        result = subprocess.run(
            ["docker", "ps"],
            capture_output=True,
            text=True,
            check=False,
        )

        return result.stdout
