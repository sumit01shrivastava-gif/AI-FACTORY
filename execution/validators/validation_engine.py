from execution.validators.pytest_validator import (
    PytestValidator,
)
from execution.validators.ruff_validator import (
    RuffValidator,
)


class ValidationEngine:

    def __init__(self):

        self.ruff = RuffValidator()

        self.pytest = PytestValidator()

    def validate(self):

        return {
            "ruff": self.ruff.validate(),
            "pytest": self.pytest.validate(),
        }
