from autonomy.evaluator import Evaluator
from autonomy.optimizer import Optimizer


class SelfImprovementEngine:

    def __init__(self):

        self.evaluator = Evaluator()

        self.optimizer = Optimizer()

    def improve(
        self,
        results,
    ):

        evaluation = self.evaluator.evaluate(
            results,
        )

        return self.optimizer.optimize(
            evaluation,
        )
