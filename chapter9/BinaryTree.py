class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(node.right, data)

    def search(self, data):
        return self._search_recursively(self.root, data)

    def _search_recursively(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursively(node.left, data)
        return self._search_recursively(node.right, data)

    def in_order_traversal(self):
        result = []
        self._in_order_recursively(self.root, result)
        return result

    def _in_order_recursively(self, node, result):
        if node:
            self._in_order_recursively(node.left, result)
            result.append(node.data)
            self._in_order_recursively(node.right, result)

    def pre_order_traversal(self):
        result = []
        self._pre_order_recursively(self.root, result)
        return result

    def _pre_order_recursively(self, node, result):
        if node:
            result.append(node.data)
            self._pre_order_recursively(node.left, result)
            self._pre_order_recursively(node.right, result)

    def post_order_traversal(self):
        result = []
        self._post_order_recursively(self.root, result)
        return result

    def _post_order_recursively(self, node, result):
        if node:
            self._post_order_recursively(node.left, result)
            self._post_order_recursively(node.right, result)
            result.append(node.data)

# Пример использования
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))  # Ожидаемый вывод: <__main__.TreeNode object at ...>
print(tree.search(20))  # Ожидаемый вывод: None

print(tree.in_order_traversal())  # Ожидаемый вывод: [5, 10, 15]
print(tree.pre_order_traversal())  # Ожидаемый вывод: [10, 5, 15]
print(tree.post_order_traversal())  # Ожидаемый вывод: [5, 15, 10]