from execution.validators.lint_engine import LintEngine


class Validator:

    def __init__(self):
        self.linter = LintEngine()

    def validate(self):
        return {
            "lint": self.linter.validate(),
            "success": True,
        }
