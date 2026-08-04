class VectorStore:

    def __init__(self):

        self.vectors = {}

    def insert(
        self,
        key,
        vector,
    ):

        self.vectors[key] = vector

    def get(
        self,
        key,
    ):

        return self.vectors.get(key)

    def all(self):

        return self.vectors
