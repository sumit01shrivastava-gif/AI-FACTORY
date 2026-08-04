import uuid


class TaskManager:

    def __init__(self):
        self.tasks = []

    def create_task(self, name, agent):

        task = {
            "id": str(uuid.uuid4()),
            "name": name,
            "agent": agent,
            "status": "pending"
        }

        self.tasks.append(task)

        return task

    def list_tasks(self):
        return self.tasks


if __name__ == "__main__":

    manager = TaskManager()

    manager.create_task(
        "Create database schema",
        "architect"
    )

    print(manager.list_tasks())
