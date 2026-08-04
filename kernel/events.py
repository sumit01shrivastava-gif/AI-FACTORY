from collections import deque


class EventBus:

    def __init__(self):
        self.events = deque()

    def publish(self, event):
        self.events.append(event)

    def consume(self):
        if self.events:
            return self.events.popleft()
        return None


if __name__ == "__main__":

    bus = EventBus()

    bus.publish(
        {
            "type": "PROJECT_CREATED",
            "project": "terrax"
        }
    )

    print(bus.consume())
