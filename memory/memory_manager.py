from datetime import datetime


class MemoryManager:

    def __init__(self):

        self.short_term_memory = []

        self.long_term_memory = []

    def remember(self, item):

        self.short_term_memory.append(
            {
                "timestamp": datetime.utcnow(),
                "data": item,
            }
        )

    def recall(self):

        return self.short_term_memory

    def clear(self):

        self.short_term_memory = []

        return True
