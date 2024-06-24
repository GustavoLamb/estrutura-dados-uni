from abc import ABC
from typing import List
from domain.graph.element import Vertex, Edge


class Graph(ABC):

    def __init__(self, vertices: int) -> None:
        if vertices <= 0:
            raise ValueError('Número de vértices não pode ser negativo ou igual a zero')

        self._vertices: int = vertices
        self._arestas: int = 0
        self._adjacentes: List[List[int]] = []
        self.clear()

    def clear(self) -> None:
        self._arestas = 0
        self._adjacentes = []
        for _ in range(self._vertices):
            self._adjacentes.append([])

    def __len__(self) -> int:
        return self._vertices

    def __str__(self) -> str:
        to_string: str = '\n'
        for i in range(1, self._vertices):
            to_string += f'[{i}] => {self._adjacentes[i]} \n'
        return to_string

    def is_empty(self) -> bool:
        return self._vertices == 0

    def add_edge(self, vertice_1: int, vertice_2: int) -> None:
        self._validate_vertice(vertice_1)
        self._validate_vertice(vertice_2)
        self._arestas += 1

    def adj(self, vertice: int) -> List[int]:
        self._validate_vertice(vertice)
        return self._adjacentes[vertice]

    def _validate_vertice(self, vertice: int) -> None:
        if not (1 <= vertice <= self._vertices):
            raise ValueError(f'Vertíce {vertice} não esta entre 1 e {self._vertices - 1}')


class WeightedGraph(ABC):
    def __init__(self, vertices: List[Vertex]) -> None:
        self.arestas: List[Edge] = []
        self.vertices: List[Vertex] = vertices

    def clear(self) -> None:
        self.arestas = []
        self.vertices = []

    def __len__(self) -> int:
        return len(self.vertices)

    def __str__(self) -> str:
        to_string: str = '\n'
        for vertice in self.vertices:
            to_string += str(vertice)
        return to_string

    def is_empty(self) -> bool:
        return self.vertices == 0

    def add_edge(self, valor: object, vertice_1: Vertex, vertice_2: Vertex) -> None:
        self._validate_vertice(vertice_1)
        self._validate_vertice(vertice_2)
        self.arestas += 1

    def _validate_vertice(self, vertice: Vertex) -> None:
        if vertice not in self.vertices:
            raise ValueError(f'Vertíce {vertice} não esta entre 1 e {self._qt_vertices}')