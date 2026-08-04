from agents.registry.agent_registry import (
    AgentRegistry,
)


def test_registry():

    registry = AgentRegistry()

    registry.register(
        "planner",
        object(),
    )

    assert registry.get(
        "planner"
    )
