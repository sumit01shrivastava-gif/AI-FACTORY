class FailureDetector:

    def detect(
        self,
        result,
    ):

        if result is None:

            return True

        if isinstance(
            result,
            dict,
        ):

            if result.get(
                "status"
            ) == "failed":

                return True

        return False
