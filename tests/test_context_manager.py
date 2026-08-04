from ai.context.context_manager import (
    ContextManager,
)


def test_context():

    manager = ContextManager()

    manager.add(
        "hello",
    )

    assert len(
        manager.retrieve()
    ) == 1
