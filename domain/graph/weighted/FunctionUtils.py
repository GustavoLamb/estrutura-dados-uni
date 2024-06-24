from domain.graph.element import Vertex, Edge


def get_weight(vertex_origem: Vertex, vertex_destino: Vertex) -> object:
    return vertex_origem.adjacentes[vertex_destino.valor].valor


def get_key_value(v: Vertex) -> object:
    return v['valor']

