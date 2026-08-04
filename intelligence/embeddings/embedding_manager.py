import hashlib


class EmbeddingManager:

    def generate(
        self,
        text,
    ):

        digest = hashlib.sha256(
            text.encode()
        ).hexdigest()

        return [
            ord(character) % 100
            for character in digest[:64]
        ]
