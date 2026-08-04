class ExecutionManager:

    def execute(
        self,
        task,
    ):

        return {
            "task": task.description,
            "status": "completed",
        }
