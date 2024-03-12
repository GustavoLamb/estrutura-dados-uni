from abc import ABC, abstractmethod


class ADTQueue(ABC):
    DEFAULT_SIZE: int = 10
    # Verifica se a fila está vazia
    @abstractmethod
    def is_empty(self) -> bool: ...
    # Verifica se a fila está cheia
    @abstractmethod
    def is_full(self) -> bool: ...
    # Insere um elemento ao final da fila
    @abstractmethod
    def enqueue(self, element: object) -> None: ...
    # Remove o elemento do início da fila
    @abstractmethod
    def dequeue(self) -> object: ...
    # Inspeciona o elemento do início da fila
    @abstractmethod
    def peek(self) -> object: ...
    @abstractmethod
    def contains(self, element: object) -> bool: ...
    # Retorna o número de elementos da fila
    @abstractmethod
    def size(self) -> int: ...