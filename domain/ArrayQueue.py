import numpy as np
from domain.abstract import ADTQueue
from exception import UnderflowError


class ArrayQueue(ADTQueue):

    def __init__(self, size: int = ADTQueue.DEFAULT_SIZE) -> None:
        self._last: int = -1
        self._elements = np.empty(size, object)

    def size(self) -> int:
        return len(self)

    def is_empty(self) -> bool:
        return self._last == -1

    def is_full(self) -> bool:
        return False

    def enqueue(self, element: object) -> None:
        if len(self) == len(self._elements):
            self._elements = np.concatenate((self._elements,
                                             np.empty(len(self._elements), object)))

        self._last += 1
        self._elements[self._last] = element

    def dequeue(self) -> object:
        if self.is_empty():
            raise UnderflowError()

        element: object = self._elements[0]
        for i in range(self._last):
            self._elements[i] = self._elements[i + 1]
        self._elements[self._last] = None
        self._last -= 1
        return element

    def peek(self) -> object:
        if self.is_empty():
            raise UnderflowError()

        return self._elements[0]

    def contains(self, element: object) -> bool:
        for elm in self:
            if elm == element:
                return True

        return False

    def flip(self):
        for indice in range(len(self) // 2):
            elemento: object = self._elements[indice]
            self._elements[indice] = self._elements[self._last - indice]
            self._elements[self._last - indice] = elemento

    def enqueue_with_priority(self, element: object):
        if len(self) == len(self._elements):
            self._elements = np.concatenate((self._elements,
                                             np.empty(len(self._elements), object)))

        for indice in range(self._last, -1, -1):
            self._elements[indice + 1] = self._elements[indice]

        self._elements[0] = element
        self._last += 1

    def __len__(self) -> int:
        return self._last + 1

    def __str__(self) -> str:
        return "[" + " ".join([str(elm) for elm in self]) + "]"

    def __iter__(self) -> object:
        for elm in self._elements[:self._last + 1]:
            yield elm
