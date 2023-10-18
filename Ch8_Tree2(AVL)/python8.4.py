# '''

# Chapter : 8 - item : 4 - Mondstadt
#  ส่งมาแล้ว 0 ครั้ง
# Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
#                 พลัง    :   5  4  4  3  2  2  2
#                 ลำดับ  :   0  1  2  3  4  5  6
# จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
#     -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
#     -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
#     -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
#     -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
#             -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
#             -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

# ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
# Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน


# Enter Input : 5 4 4 3 2 2 2/1 2,5 6,2 0
# 22
# 1>2
# 5=6
# 2<0


# Enter Input : 4 5/0 1,1 0
# 9
# 0>1
# 1<0

# '''

# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.right = None
#         self.left = None
    
# class AVLtree:

#     def __init__(self) -> None:
#         self.root = None
    

#     def insert(self, root, data):     
#         if root is None:
#             self.root = Node(data)
        
#         if root.left is None:
#             self.root.left = Node(data)
#         elif root.left is not None and root.right is None:
#             self.root.right = Node(data)
        
#     def printTree(self, node, level=0):
#         if node is not None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, str(node.data))
#             self.printTree(node.left, level + 1)

# inp = input("Enter Input : ").split('/')

# node = inp[0].split()

# avl = AVLtree()

# for i in node:
#     avl.insert(avl.root,i)

# avl.printTree(avl.root)
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self.dict = {}

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if root.left is None:
                root.left = self._insert(root.left, data)
            elif root.right is None:
                root.right = self._insert(root.right, data)
            else:
                if root.left.left is None or root.left.right is None:
                    root.left = self._insert(root.left, data)
                else:
                    root.right = self._insert(root.right, data)

            return root
    

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, str(node.data))
            self.printTree(node.left, level + 1)

# Create the binary search tree
bst = BST()
inp = input("Enter Input : ").split('/')


node = inp[0].split()

for i in node:
    bst.insert(i)
for i in range(len(node)):
    bst.dict[i] = node[i]

# Print the tree
bst.printTree(bst.root)
print(bst.dict)

# n = bst.dict

# group = []

# for i in bst.dict:
#     temp = []
#     if i not in temp:
#         temp.append(i)
#         for j in bst.dict:
#             if j == (2*i)+1 or j == (2*i)+2:
#                 temp.append(j)
#         group.append(temp)

# print(group)

