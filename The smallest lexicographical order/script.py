# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def find_longest_path(self):
        return self._find_longest_path_recursive(self.root)

    def _find_longest_path_recursive(self, node):
        if node is None:
            return []
        path = self._find_longest_path_recursive(node.right)
        path.append(node.value)
        return path

def solution(S):
    tree = BinaryTree()
    for c in S:
        tree.add(c)
    return len(S)-len(tree.find_longest_path())