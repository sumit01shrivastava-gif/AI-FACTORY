from self_healing.healing_engine import (
    HealingEngine,
)


class RecoveryManager:

    def __init__(self):

        self.healer = (
            HealingEngine()
        )

    def recover(
        self,
        error,
    ):

        return self.healer.repair(
            error,
        )
