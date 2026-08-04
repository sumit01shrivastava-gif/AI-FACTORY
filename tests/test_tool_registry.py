from tools.tool_registry import (
    ToolRegistry,
)


def test_registry():

    registry = ToolRegistry()

    registry.register(
        "tool",
        object(),
    )

    assert registry.get(
        "tool"
    ) is not None
