from domain import WayTrie


def test_count_keys_with_prefix(trie: WayTrie, prefix: str):
    print(f"Número de chaves com préfixo {prefix} é: {trie.count_keys_with_prefix(prefix)}")


def test_longest_prefix_of(trie: WayTrie, key: str):
    print(f"Maior prefixo da chave {key} é: {trie.longest_prefix_of(key)}")


def test_keys_by_pattern(trie: WayTrie, key: str):
    print(f"Lista de palavras encontradas com {key} é: {trie.keys_by_pattern(key)}")


if __name__ == '__main__':
    way_trie = WayTrie()
    lista_palavras = [('ACRE', 'Acre'), ('CASA', 'Casa'), ('CABO', 'Cabo'),
                      ('CAPA', 'Capa'), ('SALA', 'Sala'), ('SAPO', 'Sapo')]

    for chave, valor in lista_palavras:
        way_trie.insert(chave, valor)

    test_count_keys_with_prefix(way_trie, 'VA')
    test_longest_prefix_of(way_trie, "CASAMENTO")
    test_keys_by_pattern(way_trie, ".....")
