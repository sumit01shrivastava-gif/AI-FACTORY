class ScoringEngine:

    def calculate(
        self,
        score,
    ):

        if score >= 90:
            return "excellent"

        if score >= 70:
            return "good"

        return "needs_improvement"
