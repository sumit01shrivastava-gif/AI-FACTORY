class LearningEngine:

    def __init__(self):

        self.history = []

    def learn(
        self,
        result,
    ):

        self.history.append(
            result
        )

        return {
            "learned": True,
            "count": len(
                self.history
            ),
        }
