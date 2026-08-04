from runtime.sandboxes.docker_sandbox import (
    DockerSandbox,
)


class SandboxManager:

    def __init__(self):
        self.sandbox = DockerSandbox()

    def execute(self, directory):
        return self.sandbox.execute(directory)
