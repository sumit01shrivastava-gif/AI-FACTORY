class MessageBus:

    def __init__(self):

        self.messages = []

    def send(
        self,
        sender,
        receiver,
        message,
    ):
        self.messages.append(
            {
                "sender": sender,
                "receiver": receiver,
                "message": message,
            }
        )

    def receive(self):

        return self.messages
