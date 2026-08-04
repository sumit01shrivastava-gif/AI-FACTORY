class ModelManager:

    def __init__(self):

        self.models = {}

    def register(
        self,
        name,
        configuration,
    ):

        self.models[
            name
        ] = configuration

    def retrieve(
        self,
        name,
    ):

        return self.models.get(
            name
        )
