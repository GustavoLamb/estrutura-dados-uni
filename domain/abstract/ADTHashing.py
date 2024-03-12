from abc import ABC, abstractmethod


class ADTHashing(ABC):
    DEFAULT_CAPACITY: int = 10

    @abstractmethod
    def is_empty(self) -> bool: ...

    @abstractmethod
    def size(self) -> int: ...

    @abstractmethod
    def clear(self) -> None: ...

    @abstractmethod
    def insert(self, key: object, value: object) -> None: ...

    @abstractmethod
    def search(self, key: object) -> object: ...

    @abstractmethod
    def delete(self, key: object) -> bool: ...
