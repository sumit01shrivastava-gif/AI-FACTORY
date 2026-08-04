class Scheduler:

    def run(self, tasks):

        ordered = sorted(
            tasks,
            key=lambda x: x["priority"]
        )

        return ordered
