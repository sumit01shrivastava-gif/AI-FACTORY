from execution.workers.redis_queue import (
    RedisQueue,
)


class QueueManager:

    def __init__(self):
        self.queue = RedisQueue()

    def push(
        self,
        name,
        payload,
    ):
        self.queue.push(
            name,
            payload,
        )

    def pop(self, name):
        return self.queue.pop(name)
