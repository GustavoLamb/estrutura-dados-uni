class Node:
    def __init__(self, key: object, value: object) -> None:
        self.key = key
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self) -> str:
        return str(self.key)

    def next(self, other_key: object):
        return self.left if other_key < self.key else self.right


class ListNode:

    def __init__(self, element: object) -> None:
        self.element = element
        self.next: ListNode = None

    def __str__(self) -> str:
        return str(self.element)


class HashNode:

    def __init__(self, chave: object, valor: object) -> None:
        self.chave = chave
        self.valor = valor

    def __str__(self) -> str:
        return str(self.chave)
