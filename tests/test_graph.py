from knowledge.graph import Graph
from knowledge.node import Node


def test_graph():

    graph = Graph()

    graph.add_node(
        Node("1")
    )

    assert len(
        graph.nodes
    ) == 1
