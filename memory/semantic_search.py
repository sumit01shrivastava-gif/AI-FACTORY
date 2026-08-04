from memory.embedding_engine import (
    EmbeddingEngine,
)
from memory.vector_store import (
    VectorStore,
)


class SemanticSearch:

    def __init__(self):

        self.engine = EmbeddingEngine()

        self.store = VectorStore()

    def index(
        self,
        key,
        text,
    ):

        vector = self.engine.generate(
            text,
        )

        self.store.insert(
            key,
            vector,
        )

    def search(
        self,
        key,
    ):

        return self.store.get(
            key,
        )
