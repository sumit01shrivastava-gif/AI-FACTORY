class WorkflowEngine:

    def __init__(self):

        self.steps = []

    def add_step(self, step):

        self.steps.append(step)

    def execute(self):

        results = []

        for step in self.steps:

            results.append(step())

        return results
