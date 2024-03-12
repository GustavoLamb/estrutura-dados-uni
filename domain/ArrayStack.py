import numpy as np
from domain.abstract import ADTStack
from exception import UnderflowError


class ArrayStack(ADTStack):
    def __init__(self, size: int = ADTStack.DEFAULT_SIZE) -> None:
        self._top: int = -1
        self._elements = np.empty(size, object)

    def size(self) -> int:
        return len(self)

    def is_empty(self) -> bool:
        return self._top == -1

    def is_full(self) -> bool:
        return False

    def push(self, element: object) -> None:
        if len(self) == len(self._elements):
            self._elements = np.concatenate((self._elements,
                                             np.empty(len(self._elements),
                                                      object)))
        self._top += 1
        self._elements[self._top] = element

    def peek(self) -> object:
        if self.is_empty():
            raise UnderflowError()

        return self._elements[self._top]

    def pop(self) -> object:
        if self.is_empty():
            raise UnderflowError()

        element: object = self._elements[self._top]
        self._elements[self._top] = None
        self._top -= 1
        return element

    def __len__(self) -> int:
        return self._top + 1

    def __str__(self) -> str:
        return "[" + ", ".join([str(elm) for elm in self]) + "]"

    def __iter__(self) -> object:
        for elm in self._elements[self._top::-1]:
            yield elm
