class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self._insert(self.root,data)
    
    def _insert(self,root,data):
        if root is None:
            return Node(data)
        if data <= root.data:
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        return root
    
    def printPathTree(self):
        answer_list = []
        self._printPathTree(self.root,[],answer_list)
        return answer_list
    
    def _printPathTree(self,root,res,answer_list):
        if root is None:
            return
        res.append(root.data)
        if root.left is None and root.right is None:
            answer_list.append(res.copy())
        self._printPathTree(root.left,res,answer_list)
        self._printPathTree(root.right,res,answer_list)
        res.pop()

tree = BinarySearchTree()
lst = [int(i) for i in input('Enter input: ').split()]
for i in lst:
    tree.insert(i)

answer = tree.printPathTree()

answer.sort(key=lambda x: len(x), reverse=True)

print(f'{len(answer)} path(s)')

ans_dict = {}

for v in answer:
    if len(v) not in ans_dict:
        ans_dict[len(v)] = 0
    ans_dict[len(v)] += 1

for k, v in ans_dict.items():
    print(f'{v} path(s) that pass through {k-1} node(s)')