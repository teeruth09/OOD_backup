
class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()
    
    def __str__(self):
        answer = ''
        if self.list is not None:
            for i in self.list:
                answer +=i
            return answer


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self.d = {}  # Create an empty dictionary to keep track of nodes
    # def insert(self, data):
    #     self.root = self.insert_helper(self.root, data)

    # def insert_helper(self, node, data):
    #     if node is None:
    #         node = Node(data)
    #     elif node.left is None:
    #         node.left = self.insert_helper(node.left, data)
    #     elif node.left is not None and node.right is None:
    #         node.right = self.insert_helper(node.right, data)

    #     # Update the dictionary with the new node
    #     if node.data not in self.d:
    #         self.d[node.data] = node

    #     return node

    def insert(self, root, leaf):
        if root not in self.d:
            self.d[root] = Node(root)
        if leaf not in self.d:
            self.d[leaf] = Node(leaf)

        if self.d[root].left is None:
            self.d[root].left =self.d[leaf]
        else:
            self.d[root].right = self.d[leaf]

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, str(node.data))
            self.printTree(node.left, level + 1)
    
    def searchleft(self,root,stack):
        if root is None:
            return
        current = root
        while current is not None:
            stack.push(current.data)
            current = current.left
        return stack
    
    def popstack(self,stack):
        left_answer = ''
        for i in range(len(stack.list)):
            if len(stack.list) > 1:
                p = stack.pop()
                left_answer += p
        return left_answer
    
    def searchright(self,root):
        right_answer = ''
        if root is None:
            return
        current = root
        while current is not None:
            right_answer += current.data
            current = current.right
        return right_answer


s1 = Stack()
# Create an empty binary search tree
bst = BST()

# Get input from the user
inp = [x for x in input("Enter Input : ").split(",")]
top = inp[0][0]

# Process each input pair
for i in inp:
    data = i.split()
    root = data[0]
    leaf = data[1]
    # Insert the data into the binary search tree
    bst.insert(root,leaf)

# Print the binary tree with proper indentation
bst.printTree(bst.d[top])

bst.searchleft(bst.d[top],s1)
left = bst.popstack(s1)
# print(bst.searchright(bst.d[top]))
right = bst.searchright(bst.d[top])
total_string = left + right
answer = []
for i in total_string:
    answer.append(i)
    answer.append('')

print(f'Top view : {" ".join(answer)}')



# print(bst.search_last_leftmost(top))

# print(s1)



# bst = BinaryTree()
# inp = [x for x in input("Enter input: ").split(",")]

# root = []
# data = []

# print(inp)
# for i in inp:
#     list = i.split()
#     root.append(list[0])
#     data.append(list[1])
#     bst.insert(list[1],list[0])
# bst.printTree(bst.root)

# # print(root)
# # print(data)




# # bst.printTree(bst.root)


# # for i in inp:
# #     bst.insert(i)