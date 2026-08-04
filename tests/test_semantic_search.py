from memory.semantic_search import (
    SemanticSearch,
)


def test_search():

    search = SemanticSearch()

    search.index(
        "1",
        "hello world",
    )

    assert search.search(
        "1"
    ) is not None
