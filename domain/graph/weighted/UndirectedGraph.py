from domain.graph.abstract import WeightedGraph
from domain.graph.element import Vertex, Edge


class UndirectedGraph(WeightedGraph):

    def add_edge(self, valor: object, vertice_1: Vertex, vertice_2: Vertex) -> None:
        edge_1, edge_2 = Edge(vertice_2, valor), Edge(vertice_1, valor)
        vertice_1.add_edge(edge_1)
        vertice_2.add_edge(edge_2)
        self.arestas.append(edge_1)
        self.arestas.append(edge_2)
