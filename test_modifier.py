from execution.repositories.modifier import (
    RepositoryModifier,
)

modifier = RepositoryModifier()

modifier.modify(
    "test.txt",
    "AI-FACTORY TEST",
)

print("completed")
