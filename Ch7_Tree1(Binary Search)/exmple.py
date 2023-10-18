class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

def print_tree_structure(root, level=0, prefix="Root: "):
        if root is not None:
            if level > 0:
                indent = " " * (level - 1) * 4 + "+--"
            else:
                indent = ""
            print(indent + prefix + str(root.value))
            if root.left is not None or root.right is not None:
                print_tree_structure(root.right, level + 1, "R: ")
                print_tree_structure(root.left, level + 1, "L: ")


    # You can add a delete method here to remove a node if needed

# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print(bst.search(60))  # True
print(bst.search(90))  # False

print_tree_structure(bst.root)