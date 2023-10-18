class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self.insert_helper(self.root, data)
    
    def insert_helper(self, node, data):
        if node is None:
             node = Node(data)
        elif data < node.data:
            node.left = self.insert_helper(node.left, data)
        elif data > node.data:
            node.right = self.insert_helper(node.right, data)
        return node
    
    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, indent):
        if node:
            self._print_tree(node.right, indent + 5)
            print(""," " * indent + str(node.data))
            self._print_tree(node.left, indent + 5)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.data == value:
            return True
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:# value > node.data
            return self._search_recursive(node.right, value)

bst = BST()

# inp = input("Enter INput : ").split()

inp = [int(x) for x in input("Enter INput : ").split()]
for i in inp:
    bst.insert(i)
                
bst.print_tree()
print("--------------------------------------------------")
print(bst.search(10))

# def print_tree_structure(root, level=0, prefix="Root: "):
#         if root is not None:
#             if level > 0:
#                 indent = " " * (level - 1) * 4 + "+--"
#             else:
#                 indent = ""
#             print(indent + prefix + str(root.data))
#             if root.left is not None or root.right is not None:
#                 print_tree_structure(root.right, level + 1, "R: ")
#                 print_tree_structure(root.left, level + 1, "L: ")

# print_tree_structure(bst.root)