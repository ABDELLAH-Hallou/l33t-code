class TreeNode:
    def __init__(self, value, sums=None):
        self.value = value
        self.sums = sums if sums is not None else []
        self.left = None
        self.right = None

def create_tree(current_node, values, index):
    if index < len(values):

        current_node.left = TreeNode(current_node.value, current_node.sums[:])

        current_node.right = TreeNode(current_node.value + values[index], current_node.sums + [index])

        create_tree(current_node.left, values, index + 1)
        create_tree(current_node.right, values, index + 1)

def collect_sums(root, sums_map):
    if root is not None:
        if root.sums:
            if root.value not in sums_map:
                sums_map[root.value] = []
            if root.sums not in sums_map[root.value]:
                sums_map[root.value].append(root.sums)
        collect_sums(root.left, sums_map)
        collect_sums(root.right, sums_map)

def solution(A):
    root = TreeNode(0)
    create_tree(root, A, 0)
    sums_map = {}
    collect_sums(root, sums_map)
    for sum_value, paths in sums_map.items():
        unique_idx = []
        for indices in paths:
            unique_idx.extend(indices)
        if len(unique_idx) == len(A) and len(set(unique_idx)) == len(set(A)):
            return paths
