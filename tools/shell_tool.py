import subprocess


class ShellTool:

    def execute(
        self,
        command,
    ):

        return subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )
