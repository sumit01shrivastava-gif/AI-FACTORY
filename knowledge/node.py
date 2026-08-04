class Node:

    def __init__(
        self,
        identifier,
        data=None,
    ):

        self.identifier = identifier

        self.data = data or {}
