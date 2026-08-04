import hashlib


class EmbeddingEngine:

    def generate(
        self,
        text: str,
    ):

        digest = hashlib.sha256(
            text.encode()
        ).hexdigest()

        return [
            ord(character) % 100
            for character in digest[:64]
        ]
