from core.autonomous.task_manager import (
    TaskManager,
)
from core.autonomous.execution_manager import (
    ExecutionManager,
)
from memory.memory_manager import (
    MemoryManager,
)
from autonomy.self_improvement import (
    SelfImprovementEngine,
)


class AutonomousLoop:

    def __init__(self):

        self.task_manager = TaskManager()

        self.execution_manager = (
            ExecutionManager()
        )

        self.memory = MemoryManager()

        self.improvement = (
            SelfImprovementEngine()
        )

    def run_once(self):

        task = (
            self.task_manager.next_task()
        )

        if task is None:

            return None

        result = (
            self.execution_manager.execute(
                task
            )
        )

        self.memory.remember(
            result
        )

        self.improvement.improve(
            result
        )

        return result
