class TaskManager:

    def __init__(self):

        self.tasks = []

    def add_task(
        self,
        task,
    ):

        self.tasks.append(task)

    def next_task(self):

        if not self.tasks:
            return None

        return self.tasks.pop(0)
