class Extractor:

    def extract(
        self,
        text,
    ):

        return [
            word
            for word in text.split()
            if len(word) > 5
        ]
