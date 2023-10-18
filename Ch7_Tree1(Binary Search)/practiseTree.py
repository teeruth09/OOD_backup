class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_helper(self.root, data)
    
    def insert_helper(self, node, data):
        if node is None:
            node = Node(data)
        elif data < node.data:
            node.left = self.insert_helper(node.left, data)
        elif data > node.data:
            node.right = self.insert_helper(node.right, data)
        return node

    def printTree(self, node, level=1):
        if node is not None:
            self.printTree(node.right, level+1)
            print('    '* level,node.data)
            self.printTree(node.left, level+1)

    def printPreOrder(self):
        self.printPreOrderHelper(self.root)
    def printPreOrderHelper(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.printPreOrderHelper(node.left)
            self.printPreOrderHelper(node.right)
    def printInOrder(self):
        self.printInOrderHelper(self.root)
    def printInOrderHelper(self, node):
        if node is not None:
            self.printInOrderHelper(node.left)
            print(node.data, end=' ')
            self.printInOrderHelper(node.right)
    def printPostOrder(self):
        self.printPostOrderHelper(self.root)
    def printPostOrderHelper(self, node):
        if node is not None:
            self.printPostOrderHelper(node.left)
            self.printPostOrderHelper(node.right)
            print(node.data, end=' ') 


    


bst= BST()

# Create a binary search tree
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# Print the tree structure
print("Binary Search Tree:")
bst.printTree(bst.root)

# Perform preorder traversal
print("\nPreorder Traversal:")
bst.printPreOrder()  # Output: 10 5 3 7 15 12 18

# Perform inorder traversal
print("\nInorder Traversal:")
bst.printInOrder()  # Output: 3 5 7 10 12 15 18

# Perform postorder traversal
print("\nPostorder Traversal:")
bst.printPostOrder()  # Output: 3 7 5 12 18 15 10


