class Logger:

    def __init__(self):

        self.logs = []

    def write(
        self,
        message,
    ):

        self.logs.append(
            message,
        )

    def read(self):

        return self.logs
