class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self) -> str:
        return str(self.key) + nameValue(self.key)
    
def nameValue(val):
    sum = 0
    for i in [*val]:
        sum += ord(i)
    return sum

class AVL_Tree(object):

    # Function to insert a node
    def insert(self, root, key):
        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif nameValue(key) < nameValue(root.key):
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if nameValue(key) < nameValue(root.left.key):
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if nameValue(key) > nameValue(root.right.key):
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif nameValue(key) < nameValue(root.key):
            root.left = self.delete_node(root.left, key)
        elif nameValue(key) > nameValue(root.key):
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)


    def printTree(self, root, level=0):
        if root != None :
            indent = "    " * level
            print(indent + root.key,"(" + str(nameValue(root.key)) +  ")")
            self.printTree(root.left, level + 1)
            if (root.left is None and root.right is not None) or \
            (root.left is not None and root.right is None):
                print(indent + "    " + "*")
            self.printTree(root.right, level + 1)

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *key = i.split(" ")
    key = key[0] if key else ""
    if op == "I":
        root = avl_tree.insert(root, key)
    elif op == "D":
        root = avl_tree.delete_node(root, key)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")