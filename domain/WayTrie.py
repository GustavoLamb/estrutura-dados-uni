from typing import List
from domain.abstract import TrieADT


class Node:

    def __init__(self) -> None:
        self.value = None
        self.next = [None] * WayTrie.R


class WayTrie(TrieADT):
    R: int = 256

    def __init__(self) -> None:
        self._root = None

    def clear(self) -> None:
        self._root = None

    def is_empty(self) -> bool:
        return self._root is None

    def search(self, key: object) -> object:
        node: Node = self._search(self._root, key, 0)
        return node.value if node is not None else None

    def insert(self, key: object, value: object) -> None:
        def insert(current: Node, key: object, value: object, index: int) -> Node:
            if current is None:
                current = Node()
            if index == len(key):
                current.value = value
                return current
            c: int = ord(key[index])
            current.next[c] = insert(current.next[c], key, value, index + 1)
            return current

        self._root = insert(self._root, key, value, 0)

    def delete(self, key: object) -> None:
        def delete(current: Node, key: object, index: int) -> Node:
            if current is None:
                return None
            if index == len(key):
                current.value = None
            else:
                c: int = ord(key[index])
                current.next[c] = delete(current.next[c], key, index + 1)
            if current.value is not None:
                return current
            for i in range(WayTrie.R):
                if current.next[i] is not None:
                    return current
            return current

    def keys_with_prefix(self, prefix: str) -> List[str]:
        def keys_with_prefix(current: Node, prefix: str, results: List[str]) -> None:
            if current is None:
                return
            if current.value is not None:
                results.append(prefix)
            for i in range(WayTrie.R):
                prefix += chr(i)
                keys_with_prefix(current.next[i], prefix, results)
                prefix = prefix[:-1]

        results: List[str] = []
        node: Node = self._search(self._root, prefix, 0)
        keys_with_prefix(node, prefix, results)
        return results

    def count_keys_with_prefix(self, prefix: str) -> int:
        def count_keys_with_prefix(current: Node, contador: int) -> int:
            if current is None:
                return contador
            if current.value is not None:
                return contador + 1
            for i in range(WayTrie.R):
                contador = count_keys_with_prefix(current.next[i], contador)
            return contador

        contador: int = 0
        node: Node = self._search(self._root, prefix, 0)
        return count_keys_with_prefix(node, contador)

    def longest_prefix_of(self, key: str) -> str:
        def longest_prefix_of(current: Node, key: str, word: str) -> str:
            if current is None:
                return None
            if len(word) == len(key):
                return word
            index: int = len(word) if word != "" else 0
            word += key[index]
            return longest_prefix_of(current.next[ord(key[index])], key, word)
        return longest_prefix_of(self._root, key, "")
    
    def keys_by_pattern(self, pattern: str) -> List[str]:
        def keys_by_pattern(node: Node, current_word: str, pattern_index: int, results: List[str]) -> None:
            if node is None:
                return

            if pattern_index == len(pattern):
                if node.value is not None:
                    results.append(current_word)
                return

            current_char = pattern[pattern_index]
            if current_char == '.':
                for child in node.next:
                    if child is not None:
                        keys_by_pattern(child, current_word + chr(node.next.index(child)), pattern_index + 1, results)
            else:
                child = node.next[ord(current_char)]
                if child is not None:
                    keys_by_pattern(child, current_word + current_char, pattern_index + 1, results)

        results: List[str] = []
        keys_by_pattern(self._root, "", 0, results)

        return results if len(results) > 0 else None

    def _search(self, current: Node, key: object, index: int) -> Node:
        if current is None:
            return None
        elif index == len(key):
            return current
        return self._search(current.next[ord(key[index])], key, index + 1)
