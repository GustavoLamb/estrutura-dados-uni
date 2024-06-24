from domain.graph.abstract import Graph


class UndirectedGraph(Graph):

    def add_edge(self, vertice_1: int, vertice_2: int) -> None:
        super().add_edge(vertice_1, vertice_2)
        self._adjacentes[vertice_1].append(vertice_2)
        self._adjacentes[vertice_2].append(vertice_1)
