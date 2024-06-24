from domain.graph.abstract import WeightedGraph
from domain.graph.element import Vertex, Edge


class DirectedGraph(WeightedGraph):

    def add_edge(self, valor: object, vertice_1: Vertex, vertice_2: Vertex) -> None:
        edge_1 = Edge(vertice_2, valor)
        vertice_1.add_edge(edge_1)
        self.arestas.append(edge_1)
