from knowledge.edge import Edge


class RelationshipManager:

    def connect(
        self,
        graph,
        source,
        target,
    ):

        graph.add_edge(
            Edge(
                source,
                target,
            )
        )
