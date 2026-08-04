class DependencyManager:

    def __init__(self):

        self.dependencies = {}

    def add(
        self,
        task,
        dependency,
    ):

        self.dependencies.setdefault(
            task,
            [],
        ).append(
            dependency,
        )
