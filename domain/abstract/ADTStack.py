from abc import ABC, abstractmethod


class ADTStack(ABC):
    DEFAULT_SIZE: int = 10
    # Quantos elementos há na pilha
    @abstractmethod
    def size(self) -> int: ...
    # Pilha está vazia?
    @abstractmethod
    def is_empty(self) -> bool: ...
    # Pilha está cheia?
    @abstractmethod
    def is_full(self) -> bool: ...
    # Insere um elemento no topo da pilha
    @abstractmethod
    def push(self, element: object) -> None: ...
    # Remove o elemento do topo da pilha
    @abstractmethod
    def pop(self) -> object: ...
    # Inspeciona/Retorna o elemento do topo da pilha
    @abstractmethod
    def peek(self) -> object: ...


