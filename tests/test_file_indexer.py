from indexing.file_indexer import (
    FileIndexer,
)


def test_indexer():

    indexer = FileIndexer()

    result = indexer.index()

    assert isinstance(
        result,
        list,
    )
