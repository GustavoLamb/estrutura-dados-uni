from abc import ABC, abstractmethod


class ADTList(ABC):

    DEFAULT_SIZE: int = 10
    @abstractmethod
    def size(self) -> int: ...

    @abstractmethod
    def is_empty(self) -> bool: ...

    @abstractmethod
    def is_full(self) -> bool: ...

    @abstractmethod
    def insert(self, element: object, pos: int) -> None: ...

    @abstractmethod
    def insert_first(self, element: object) -> None: ...

    @abstractmethod
    def insert_last(self, element: object) -> None: ...

    @abstractmethod
    def remove(self, pos: int) -> object: ...

    @abstractmethod
    def remove_first(self) -> object: ...

    @abstractmethod
    def remove_last(self) -> object: ...

    @abstractmethod
    def get(self, pos: int) -> object: ...

    @abstractmethod
    def search(self, element: object) -> int: ...
    