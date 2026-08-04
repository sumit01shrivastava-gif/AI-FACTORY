class Ranker:

    def rank(
        self,
        items,
    ):

        return sorted(
            items,
            key=len,
            reverse=True,
        )
