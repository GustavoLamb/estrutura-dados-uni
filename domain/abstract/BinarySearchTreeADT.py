from abc import ABC, abstractmethod


class BinarySearchTreeADT(ABC):
    @abstractmethod
    def clear(self) -> None:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def search(self, key: object) -> object:
        ...

    @abstractmethod
    def insert(self, key: object, value: object) -> None:
        ...

    @abstractmethod
    def delete(self, key: object) -> bool:
        ...

    @abstractmethod
    def pre_order_transversal(self) -> None:
        ...

    @abstractmethod
    def in_order_transversal(self) -> None:
        ...

    @abstractmethod
    def post_order_transversal(self) -> None:
        ...

    @abstractmethod
    def level_order_transversal(self) -> None:
        ...

    @abstractmethod
    def size(self) -> int:
        ...

    @abstractmethod
    def degree(self, key: object) -> int:
        ...
