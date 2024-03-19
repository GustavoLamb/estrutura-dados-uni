class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)


def array_to_tree(array) -> Node:
    def insert(root, index) -> Node:
        if index < len(array):
            root = Node(array[index])
            root.left = insert(root.left, index * 2 + 1)
            root.right = insert(root.right, index * 2 + 2)
        return root
    return insert(None, 0)


def tree_to_array(root: Node):
    answer = [root.key]
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            answer.append(node.left.key)
            queue.append(node.left)
        if node.right:
            answer.append(node.right.key)
            queue.append(node.right)
    return answer


if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 6, 9]
    root = array_to_tree(array)
    print(f'Root: {root}, Child Left: {root.left}, Child Right: {root.right}')
    print('Array:', *tree_to_array(root))


