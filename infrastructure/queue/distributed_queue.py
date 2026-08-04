class DistributedQueue:

    def __init__(self):

        self.queue = []

    def push(
        self,
        item,
    ):

        self.queue.append(item)

    def pop(self):

        if self.queue:

            return self.queue.pop(0)

        return None
