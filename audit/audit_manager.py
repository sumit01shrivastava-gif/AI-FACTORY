class AuditManager:

    def __init__(self):

        self.records = []

    def log(
        self,
        event,
    ):

        self.records.append(
            event,
        )

    def retrieve(self):

        return self.records
