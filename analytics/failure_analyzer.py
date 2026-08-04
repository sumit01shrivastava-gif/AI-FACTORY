class FailureAnalyzer:

    def analyze(
        self,
        error,
    ):

        return {
            "error": str(error),
            "resolved": False,
        }
