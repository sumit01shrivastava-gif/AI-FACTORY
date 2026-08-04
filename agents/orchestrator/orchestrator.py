from execution.executor import Executor
from execution.validators.validation_engine import (
    ValidationEngine,
)
from execution.repositories.commit_manager import (
    CommitManager,
)
from execution.repositories.push_manager import (
    PushManager,
)
from runtime.sandboxes.sandbox_manager import (
    SandboxManager,
)


class Orchestrator:

    def __init__(self):

        self.executor = Executor()

        self.validator = ValidationEngine()

        self.committer = CommitManager()

        self.pusher = PushManager()

        self.sandbox = SandboxManager()

    def execute(self, directory):

        sandbox_result = self.sandbox.execute(
            directory,
        )

        validation_result = (
            self.validator.validate()
        )

        return {
            "sandbox": sandbox_result,
            "validation": validation_result,
        }
