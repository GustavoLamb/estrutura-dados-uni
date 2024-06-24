from domain.graph.element import Vertex


class Edge:

    def __init__(self, vertice_destino: Vertex, valor: object = None, vertice_origem: Vertex = None):
        self.valor = valor
        self.vertice_destino = vertice_destino
        self.vertice_origem = vertice_origem

    def __str__(self):
        return f'Edge(destino={self.vertice_destino}, valor={self.valor})'

    def __repr__(self):
        return f'Edge(destino={self.vertice_destino.valor}, valor={self.valor})'
