from core.task import Task
from core.autonomous.autonomous_loop import (
    AutonomousLoop,
)


def test_loop():

    loop = AutonomousLoop()

    loop.task_manager.add_task(
        Task(
            "1",
            "test",
        )
    )

    result = loop.run_once()

    assert result is not None
