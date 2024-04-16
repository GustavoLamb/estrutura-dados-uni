from domain import WayTrie


def test_count_keys_with_prefix(trie: WayTrie, prefix: str):
    print(f"Número de chaves com préfixo {prefix} é: {trie.count_keys_with_prefix(prefix)}")


if __name__ == '__main__':
    way_trie = WayTrie()
    lista_palavras = [('ACRE', 'Acre'), ('CASA', 'Casa'), ('CABO', 'Cabo'),
                      ('CAPA', 'Capa'), ('SALA', 'Sala'), ('SAPO', 'Sapo')]

    for palavra in lista_palavras:
        way_trie.insert(palavra[0], palavra[1])

    test_count_keys_with_prefix(way_trie, 'CA')
