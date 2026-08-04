class Graph:

    def __init__(self):

        self.nodes = {}

        self.edges = []

    def add_node(
        self,
        node,
    ):

        self.nodes[node.identifier] = node

    def add_edge(
        self,
        edge,
    ):

        self.edges.append(edge)
