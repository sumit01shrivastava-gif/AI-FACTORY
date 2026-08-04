from memory.memory_manager import MemoryManager


def test_memory():

    memory = MemoryManager()

    memory.remember("hello")

    result = memory.recall()

    assert len(result) == 1
