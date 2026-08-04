class ExecutionPipeline:

    def __init__(self):

        self.stages = []

    def add_stage(
        self,
        stage,
    ):

        self.stages.append(stage)

    def execute(self):

        results = []

        for stage in self.stages:

            results.append(stage())

        return results
