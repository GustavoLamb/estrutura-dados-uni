import numpy as np
from domain.abstract import ADTHashing
from domain import HashNode
from exception import OverflowError


class ClosedHashing(ADTHashing):

    def __init__(self, capacity: int = ADTHashing.DEFAULT_CAPACITY):
        self._max_capacity: int = capacity
        self._total_elements: int = 0
        self._table = np.empty(self._max_capacity, HashNode)

    def insert(self, key: object, value: object) -> None:

        def insert(chave: object, valor: object, indice: int):

            hash_code = self._hashing(chave, indice)

            if indice > 0 and hash_code == self._hashing(chave, 0):
                raise OverflowError("Limite da tabela atingido! =(")

            if self._table[hash_code]:
                insert(chave, valor, indice + 1)
            else:
                self._table[hash_code] = HashNode(chave, valor)
                self._total_elements += 1

        insert(key, value, 0)

    def search(self, key: object) -> object:

        def search(chave: object, indice: int):

            hash_code: int = self._hashing(chave, indice)

            if indice > 0 and hash_code == self._hashing(chave, 0):
                return None

            if self._table[hash_code] and self._table[hash_code].chave == chave:
                return self._table[hash_code].valor

            return search(chave, indice + 1)

        return search(key, 0)

    def delete(self, key: object) -> bool:

        def delete(chave: object, indice: int):

            hash_code = self._hashing(chave, indice)

            if indice > 0 and hash_code == self._hashing(chave, 0):
                return False

            if self._table[hash_code] and self._table[hash_code].chave == chave:
                self._table[hash_code] = None
                self._total_elements -= 1

                return True

        return delete(key, 0)

    def is_empty(self) -> bool:
        return self._total_elements == 0

    def size(self) -> int:
        return self._total_elements

    def clear(self) -> None:
        self._total_elements = 0

        self._table = np.empty(self._max_capacity, HashNode)

    def __str__(self) -> str:
        return "[" + ", ".join([str(elm) for elm in self]) + "]"

    def __iter__(self) -> object:
        for elm in self._table[:self._max_capacity + 1]:
            yield elm if elm else '_'

    def _hashing(self, key: object, indice: int) -> int:
        k: int = (hash(key) & 0x7fffffff)
        return self._doubleProbing(k, indice)

    def _doubleProbing(self, key: int, indice: int) -> int:
        return ((key % self._max_capacity) + indice * (1 + key % (self._max_capacity - 1))) % self._max_capacity

    def _linearProbing(self, key: int, indice: int) -> int:
        return (key + indice) % self._max_capacity

    def _quadraticProbing(self, key: int, indice: int):
        return (key + indice ** 2) % self._max_capacity
