from domain.abstract import ADTStack
from domain import ListNode
from exception import UnderflowError


# Nomes: Gustavo Herique Lamb, Arthur Cosme da Silva, Gregory Stein, Felipe Freitas,
# Reury Pereira timm e Ricardo Moreira Gomes.
class LinkedStack(ADTStack):
    def __init__(self):
        self._head: ListNode = None
        self._tail: ListNode = None
        self._count = 0

    def size(self) -> int:
        return len(self)

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return False

    def push(self, element: object) -> None:
        new_node: ListNode = ListNode(element)

        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head

        self._head = new_node
        self._count += 1

    def pop(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        element: object = self._head.element
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._count -= 1

        return element

    def peek(self) -> object:
        return self._head.element

    def __len__(self):
        return self._count

    def __str__(self) -> str:
        return "[" + " ".join([str(node) for node in self]) + "]"

    def __iter__(self) -> object:
        current: ListNode = self._head
        while current:
            yield current.element
            current = current.next
