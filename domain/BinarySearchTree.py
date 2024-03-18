from domain.abstract import BinarySearchTreeADT
from domain.Node import Node


class BinarySearchTree(BinarySearchTreeADT):

    def __init__(self, root: Node = None) -> None:
        self._root: Node = root

    def clear(self) -> None:
        self._root = None

    def is_empty(self) -> bool:
        return self._root is None

    def search(self, key: object) -> object:
        def search(current: Node, key: object) -> object:
            if current is None:
                return None
            elif key == current.key:
                return current.value
            return search(current.next(key), key)

        return search(self._root, key)

    def insert(self, key: object, value: object) -> None:
        def insert(current: Node, key: object, value: object) -> Node:
            if current is None:
                return Node(key, value)
            elif key > current.key:
                current.right = insert(current.right, key, value)
            elif key < current.key:
                current.left = insert(current.left, key, value)
            return current

        self._root = insert(self._root, key, value)

    def delete(self, key: object) -> bool:
        return self._delete_by_copying(key)

    def pre_order_transversal(self) -> None:
        def pre_order_transversal(current: Node) -> None:
            if current:
                print(current.key, end=' ')
                pre_order_transversal(current.left)
                pre_order_transversal(current.right)

        pre_order_transversal(self._root)

    def in_order_transversal(self) -> None:
        def in_order_transversal(current: Node) -> None:
            if current:
                in_order_transversal(current.left)
                print(current.key, end=' ')
                in_order_transversal(current.right)

        in_order_transversal(self._root)

    def post_order_transversal(self) -> None:
        def post_order_transversal(current: Node) -> None:
            if current:
                post_order_transversal(current.left)
                post_order_transversal(current.right)
                print(current.key, end=' ')

        post_order_transversal(self._root)

    def level_order_transversal(self) -> None:
        if self._root:
            queue = [self._root]
            while queue:
                current: Node = queue.pop(0)
                print(current.key, end=' ')
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

    def size(self) -> int:
        def size(current: Node) -> int:
            if current is None:
                return 0

            return 1 + size(current.left) + size(current.right);

        return size(self._root)

    def descendent(self, key: object) -> str:
        descendent_queue = []

        def descendent(current: Node) -> None:
            if current:
                descendent(current.left)
                descendent_queue.append(current)
                descendent(current.right)

        parrent: Node = self._search_node(key)
        descendent(parrent)

        return ' '.join(f'{numero}' for numero in descendent_queue) if len(descendent_queue) > 0 else None

    def degree(self, key: object) -> int:
        def degree(current: Node, key: object) -> int:
            if current is None:
                return -1

            if current.key == key:
                left_node = 1 if current.left else 0
                right_node = 1 if current.right else 0
                return left_node + right_node

            return degree(current.next(key), key)

        return degree(self._root, key)

    def height(self, key: object) -> int:
        def height(current: Node, key: object) -> int:
            if current is None:
                return -1
            
            if current.key == key:
                return self._height(current)
            
            left_node = height(current.left, key)
            right_node = height(current.right, key)

            if left_node == -1 and right_node == -1:
                return -1
            elif left_node == -1:
                return right_node
            elif right_node == -1:
                return left_node
            else:
                return min(left_node, right_node)
        return height(self._root, key)

    def depth(self, key: object) -> int:
        def depth(current: Node, key: object, count: int) -> int:
            if current is None:
                return -1
            if current.key == key:
                return count
            count += 1
            return depth(current.next(key), key, count)
        return depth(self._root, key, 0)

    def _height(self, current: Node):
        if current is None:
            return -1

        left_node = self._height(current.left)
        right_node = self._height(current.right)

        return 1 + max(left_node, right_node)

    def _delete_by_copying(self, key: object) -> bool:
        parent: Node = None
        current: Node = None
        parent, current = self._get_parent(key)
        if current is None:
            return False

        # Case 3
        elif current.left and current.right:
            at_the_right: Node = current.left
            while at_the_right.right:
                at_the_right = at_the_right.right
            self._delete_by_copying(at_the_right.key)
            current.key, current.value = at_the_right.key, at_the_right.value

        # Case 1 e 2
        else:
            next_node: Node = current.left or current.right
            if current == self._root:
                self._root = next_node
            elif current == parent.left:
                parent.left = next_node
            else:
                parent.right = next_node

        return True

    def _delete_by_merging(self, key: object):
        parent: Node = None
        current: Node = None
        parent, current = self._get_parent(key)
        if current is None:
            return False
        # Case 3
        elif current.left and current.right:
            at_the_right: Node = current.left
            while at_the_right.right:
                at_the_right = at_the_right.right
            at_the_right.right = current.right

            if current == self._root:
                self._root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        # Case 1 e 2
        else:
            next_node: Node = current.left or current.right
            if current == self._root:
                self._root = next_node
            elif current == parent.left:
                parent.left = next_node
            else:
                parent.right = next_node

        return True

    def _search_node(self, key) -> Node:
        def search_node(current: Node, key: object) -> Node:
            if current is None:
                return None

            elif key == current.key:
                return current

            return search_node(current.next(key), key)

        return search_node(self._root, key)

    def _get_parent(self, key: object) -> tuple[Node, Node]:
        parent: Node = None
        current: Node = self._root
        while current and key != current.key:
            if key != current.key:
                parent = current
                current = current.next(key)

        return parent, current

    def __str__(self) -> str:
        return '[empty]' if self.is_empty() else self._str_tree()

    def _str_tree(self) -> str:
        def _str_tree(current: Node, is_right: bool, tree: str, ident: str) -> str:

            if current.right:
                tree = _str_tree(current.right, True, tree, ident + (' ' * 8 if is_right else ' |' + ' ' * 6))

            tree += ident + (' /' if is_right else ' \\') + '-----' + str(current) + '\n'

            if current.left:
                tree = _str_tree(current.left, False, tree, ident + (' |' + ' ' * 6 if is_right else ' ' * 8))

            return tree

        tree: str = ''
        if self._root.right:
            tree = _str_tree(self._root.right, True, tree, '')
        tree += str(self._root) + '\n'
        if self._root.left:
            tree = _str_tree(self._root.left, False, tree, '')

        return tree
