from util import array_to_tree


def print_tree_array(array) -> None:
    root = array_to_tree(array)
    print_tree_node(root)


def print_tree_node(root) -> None:
    def str_tree(current, is_right: bool, tree: str, ident: str) -> str:

        if current.right:
            tree = str_tree(current.right, True, tree, ident + (' ' * 8 if is_right else ' |' + ' ' * 6))

        tree += ident + (' /' if is_right else ' \\') + '-----' + str(current) + '\n'

        if current.left:
            tree = str_tree(current.left, False, tree, ident + (' |' + ' ' * 6 if is_right else ' ' * 8))

        return tree

    tree: str = ''
    if root.right:
        tree = str_tree(root.right, True, tree, '')
    tree += str(root) + '\n'
    if root.left:
        tree = str_tree(root.left, False, tree, '')

    print(tree)


if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 6, 9]
    print_tree_array(array)
