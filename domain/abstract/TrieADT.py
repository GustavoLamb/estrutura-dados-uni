from abc import ABC, abstractmethod
from typing import List


class TrieADT(ABC):

    @abstractmethod
    def clear(self) -> None: ...

    @abstractmethod
    def is_empty(self) -> bool: ...

    @abstractmethod
    def search(self, key: object) -> object: ...

    @abstractmethod
    def insert(self, key: object, value: object) -> None: ...

    @abstractmethod
    def delete(self, key: object) -> None: ...

    @abstractmethod
    def keys_with_prefix(self, prefix: str) -> List[str]: ...

    @abstractmethod
    def count_keys_with_prefix(self, prefix: str) -> int: ...

    @abstractmethod
    def longest_prefix_of(self, key: str) -> str: ...

    # @abstractmethod
    # def keys_by_pattern(self, pattern: str) -> List[str]: ...
