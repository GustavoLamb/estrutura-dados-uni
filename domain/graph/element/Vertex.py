from domain.graph.element import Edge
from typing import Dict


class Vertex:

    def __init__(self, valor: object) -> None:
        self.d = None
        self.pi = None
        self.valor: object = valor
        self.adjacentes: Dict[object, Edge] = {}

    def add_edge(self, edge: Edge) -> None:
        edge.vertice_origem = self
        self.adjacentes[edge.vertice_destino.valor] = edge

    def __

    def __eq__(self, other: object):
        return self.valor == other

    def __str__(self) -> str:
        return f'[{self.valor}] => {list(self.adjacentes.values())} \n'

    def __repr__(self) -> str:
        return f'[{self.valor}] => {list(self.adjacentes.values())} \n'
