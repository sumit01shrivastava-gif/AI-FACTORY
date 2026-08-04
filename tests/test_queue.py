from infrastructure.queue.distributed_queue import (
    DistributedQueue,
)


def test_queue():

    queue = DistributedQueue()

    queue.push("task")

    assert queue.pop() == "task"
