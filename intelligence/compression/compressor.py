class Compressor:

    def compress(
        self,
        text,
        limit=50,
    ):

        if len(text) <= limit:

            return text

        return text[:limit]
