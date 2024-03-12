from domain import ListNode
from domain.abstract import ADTList
from exception import UnderflowError


class SinglyLinkedList(ADTList):

    def __init__(self) -> None:
        self._head: ListNode = None
        self._tail: ListNode = None
        self._count: int = 0

    def size(self) -> int:
        return len(self)

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return False

    def insert_first(self, element: object) -> None:
        new_node: ListNode = ListNode(element)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
        self._head = new_node
        self._count += 1

    def insert_last(self, element: object) -> None:
        new_node: ListNode = ListNode(element)

        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._count += 1

    def insert(self, element: object, pos: int) -> None:
        if pos < 0 or pos > self._count:
            raise IndexError()

        if pos == 0:
            self.insert_first(element)
        elif pos == self._count:
            self.insert_last(element)
        else:
            prev: ListNode = self._head
            for _ in range(0, pos - 1):
                prev = prev.next
            new_node: ListNode = ListNode(element)
            new_node.next = prev.next
            prev.next = new_node
            self._count += 1

    def add_after(self, element: object, pos: int):
        self.insert(element, pos + 1)

    def add_before(self, element: object, pos: int):
        self.insert(element, pos)

    def split(self, pos: int):
        if pos < 0 or pos >= self._count:
            raise IndexError()

        new_list: SinglyLinkedList = SinglyLinkedList()
        current_node = self._head
        for _ in range(0, pos):
            new_list.insert_last(current_node)
            current_node = current_node.next

        self._head = current_node

        return new_list

    def remove_first(self) -> object:
        if self.is_empty():
            raise UnderflowError()

        element: object = self._head.element
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
        self._count -= 1
        return element

    def remove_last(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        element: object = self._tail.element
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            prev: ListNode = self._head
            while prev.next != self._tail:
                prev = prev.next
            self._tail = prev
            prev.next = None
            self._count -= 1
            return element

    def remove(self, pos: int) -> object:
        if self.is_empty():
            raise UnderflowError()

        if pos < 0 or pos >= self._count:
            raise IndexError()
        if pos == 0:
            return self.remove_first()
        elif pos == self._count - 1:
            return self.remove_last()
        else:
            prev: ListNode = self._head
            for _ in range(0, pos - 1):
                prev = prev.next
            element: object = prev.next.element
            prev.next = prev.next.next
            self._count -= 1
            return element

    def search(self, element: object) -> int:
        for i, elm in enumerate(self):
            if elm == element:
                return i
        return -1

    def get(self, pos: int) -> object:
        if pos < 0 or pos >= self._count:
            raise IndexError()

        current: ListNode = self._head
        for _ in range(0, pos):
            current = current.next
        return current.element

    def other_get(self, pos: int) -> object:
        if pos < 0 or pos >= self._count:
            raise IndexError()
        for i, elm in enumerate(self):
            if i == pos:
                return elm

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return "[" + " ".join([str(node) for node in self]) + "]"

    def __iter__(self) -> object:
        current: ListNode = self._head
        while current:
            yield current.element
            current = current.next

