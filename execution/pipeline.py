from execution.executor import Executor
from execution.validators.validator import Validator
from scanners.context_engine import ContextEngine


class Pipeline:

    def run(self):

        context = ContextEngine()

        executor = Executor()

        validator = Validator()

        print(context.build("terrax"))

        print(
            executor.execute(
                "terrax",
                "Create authentication module",
                "Next.js",
            )
        )

        print(validator.validate())
