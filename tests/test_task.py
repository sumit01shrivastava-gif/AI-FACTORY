from core.task import Task


def test_task():

    task = Task(
        "1",
        "Build API",
    )

    assert (
        task.status == "pending"
    )
