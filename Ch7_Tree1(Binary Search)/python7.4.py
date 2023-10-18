'''
Chapter : 7 - item : 4 - Top of The Tree (3T)
 ส่งมาแล้ว 0 ครั้ง
    มีเด็กหนุ่มชื่อ Jimmy ที่นั่งอยู่บนพื้นห้องของเขา แต่มองลงมาที่พื้นไม่ได้เหมือนคนปกติ แต่เขามีการมองแบบเฉพาะหนึ่งแบบ ด้วยหลักการของการมองแบบ Top View จาก Binary Search Tree

ในห้องของ Jimmy มีสัญลักษณ์ต่างๆ กระจายอยู่บนพื้น แต่มันไม่มีลำดับการเรียงที่แน่นอน เหมือนใน Binary Search Tree ที่มีโครงสร้างของลูกข้างข้างและการเรียงลำดับที่ชัดเจน

Jimmy มีความสามารถพิเศษที่สามารถมองเห็นสัญลักษณ์ที่อยู่บนพื้นอย่างเฉพาะเจาะจง เขาสามารถมองเห็นเฉพาะสัญลักษณ์ที่อยู่บนสุดของสัญลักษณ์ที่วางอยู่ได้ และมองเห็นเฉพาะสัญลักษณ์ที่อยู่บนสุดของแต่ละส่วนของสัญลักษณ์

เรื่องราวของ Jimmy นี้สอนให้เราเห็นว่าความสามารถในการมองแบบ Top View จาก Binary Search Tree สามารถนำไปใช้กับการมองเห็นโลกในมุมที่เราไม่เคยเห็นมาก่อน และช่วยให้เราเข้าใจโลกในมุมต่างๆ ได้มากขึ้น

พี่ๆสงสัยว่า มุมมองแบบ Top View ของ Jimmy จะมองเห็นเป็นอย่างไร ช่วยพี่ด้วย พี่อยากเห็น!!!

หลักการสั้นๆ :
   1. สร้าง Binary Search Tree ขึ้นมา
   2. ให้ Element แรกที่ได้รับมาเป็น Root เสมอ
   3. หา Element ที่ต้องการเชื่อม
   4. ถ้าซ้ายยังว่าง ใส่เข้าไปทางซ้ายก่อนเสมอ
   5. แต่ถ้าไม่ว่าง ก็ใส่ทางขวาแทน
   6. พอสร้าง Binary Tree เสร็จ ก็ลองบอกมุมมอง Top View ของ Jimmy ให้พี่ดูหน่อย

หมายเหตุ : Binary Tree อันนี้ไม่ได้ใช้แบบ inorder นะครับ ระวังไว้นะน้องๆ
หมายเหตุ 2: ตรงที่ไฮไลท์ไว้สำคัญมากอ่านด้วย ไม่งั้นจะไม่เข้าใจโจทย์นะน้อง


Enter Input : 1 2,1 3,2 4,2 5,3 6,3 7
Top view : 4 2 1 3 7 


Enter Input : a b,a c,c d,b e
Top view : e b a c 


Enter Input : v o,v e,o l,e x,e u,l i
Top view : i l o v e u 


'''
class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self.d = {}  # Create an empty dictionary to keep track of nodes
    
    def insert(self, root, leaf):
        if root not in self.d:
            self.d[root] = Node(root)
        if leaf not in self.d:
            self.d[leaf] = Node(leaf)

        if self.d[root].left is None:
            self.d[root].left =self.d[leaf]
        elif self.d[root].left is not None and self.d[root].right is None:
            self.d[root].right = self.d[leaf]

        if self.d[root].left is not None and self.d[root].right is not None:
            pass

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
    

    def topView(self, root):
        if root is None:
            return []

        # Use a dictionary to store nodes at each horizontal distance from the root
        # The horizontal distance of the root is 0
        hd_dict = {}
        queue = [(root, 0)]

        while queue:
            node, hd = queue.pop(0)

            # If the horizontal distance is not in the dictionary, add the node to it
            if hd not in hd_dict:
                hd_dict[hd] = node.data

            # Traverse left child with a horizontal distance of hd - 1
            if node.left:
                queue.append((node.left, hd - 1))

            # Traverse right child with a horizontal distance of hd + 1
            if node.right:
                queue.append((node.right, hd + 1))

        # Sort the keys (horizontal distances) and print the corresponding values
        sorted_keys = sorted(hd_dict.keys())
        top_view = [hd_dict[hd] for hd in sorted_keys]

        return top_view
    

s1 = Stack()
# Create an empty binary search tree
bst = BST()

# Get input from the user
inp = [x for x in input("Enter Input : ").split(",")]


first_inp = inp[0].split()

top = first_inp[0]

# Process each input pair
for i in inp:
    data = i.split()
    root = data[0]
    leaf = data[1]
    
    # Insert the data into the binary search tree
    bst.insert(root,leaf)

# bst.printTree(bst.d[top])

bst.searchleft(bst.d[top],s1)
left = bst.popstack(s1)

right = bst.searchright(bst.d[top])
total_string = left + right
answer = []
for i in total_string:
    answer.append(i)
    
# print(answer)
bst.printTree(bst.d[top])
print(f'Top view : {" ".join(answer)}')
print(bst.topView(bst.d[top]))