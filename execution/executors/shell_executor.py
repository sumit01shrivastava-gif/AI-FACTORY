import subprocess


class ShellExecutor:
    def run(self, command, cwd=None):
        try:
            result = subprocess.run(
    command,
    shell=True,
    check=False,
                cwd=cwd,
                capture_output=True,
                text=True,
            )

            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }

        except subprocess.SubprocessError as e:
            return {
                "success": False,
                "error": str(e),
            }


if __name__ == "__main__":
    executor = ShellExecutor()

    print(executor.run("pwd"))
