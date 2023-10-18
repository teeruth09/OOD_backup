class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self.insert_helper(self.root, data)
    def insert_helper(self, node, data):
        if node is None:
            node = Node(data)
        elif data < node.data:
            node.left = self.insert_helper(node.left, data)
        elif data >= node.data:
            node.right = self.insert_helper(node.right, data)
        return node
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