from domain import BinarySearchTree


def test_descendent_no_bst(binary_search_tree: BinarySearchTree, key: object):
    print(binary_search_tree.descendent(key))


def test_grau_no_bst(binary_search_tree: BinarySearchTree, key: object):
    print(f'Grau do nó {key} é:', binary_search_tree.degree(key))


def test_tamanho_binary_search_tree(binary_search_tree: BinarySearchTree):
    print("Tamanho da árvore é de:", binary_search_tree.size())


def test_operacoes_gerais_bst(binary_tree: BinarySearchTree):
    # Procurando chave 14, mostra valor 7:
    print("Procurnando valor da  chave 14:", binary_tree.search(14))

    # Inserindo chave na direita 16, com valor 8
    print("Inserindo chave na direita 16, com valor 8: ")
    binary_tree.insert(16, 8)
    print(binary_tree)

    # Inserindo chave na esquerda 1, com valor 0.5
    print("Inserindo chave na direita 16, com valor 8: ")
    binary_tree.insert(1, 0.5)
    print(binary_tree)

    # Caso 1 de exclusão:
    print("Excluindo chave 1 que é uma folha, nó 2 sem filho")
    binary_tree.delete(1)
    print(binary_tree)

    # Caso 2 de exclusão:
    print("Excluindo chave 14 com um filho 16, chave 12 tem filho da direita 16: ")
    binary_tree.delete(14)
    print(binary_tree)

    # Caso 3 de exclusão:
    print("Excluindo chave 12 com dois filhos: 16 e 10, chave 10 assume lugar do 12, com filho 16:")
    binary_tree.delete(12)
    print(binary_tree)

    print("Percurso de profundiade pré ordem: ")
    binary_tree.pre_order_transversal()

    print("\nPercurso de profundiade em ordem: ")
    binary_tree.in_order_transversal()

    print("\nPercurso de profundiade pós ordem: ")
    binary_tree.post_order_transversal()

    print("\nPercurso de amplitudo em nível: ")
    binary_tree.level_order_transversal()


def main() -> None:
    binary_tree: BinarySearchTree = BinarySearchTree()
    # Inicializando a árvore
    for key in [8, 4, 2, 6, 12, 10, 14]:
        binary_tree.insert(key, key // 2)

    print(binary_tree)
    test_descendent_no_bst(binary_tree, 22)
    # test_grau_no_bst(binary_tree, 22)
    # test_tamanho_binary_search_tree(binary_tree)
    # test_operacoes_gerais_bst(binary_tree)


if __name__ == '__main__':
    main()
