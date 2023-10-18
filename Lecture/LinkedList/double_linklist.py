class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoubleLinklist:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = ""
        current = self.head
        while current:
            s += str(current.data)
            current = current.next #move to next node
            if current is not None:
                s += "->"
        return s
    

    def append(self,data): #เพิ่มข้อมูลเข้าทางท้าย
        # new_node = Node(data)
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next: #ถ้ามี node ถัดไป
                current = current.next   # head = node ถัดไป
            current.next = new_node
            new_node.prev = current #node เก่า = head
            new_node.next = None 
    
    def prepend(self,data): #เพิ่มข้อมูลเข้าทางด้านหน้า
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node #ตัวก่อนหน้า head = node ใหม่
            new_node.next = self.head #next node ต้องเปลี่ยนเป็น head
            self.head = new_node
            print(self.head.data)
            new_node.prev = None    

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def add_after_node(self, key, data): #ใส่ข้อมูลหลัง key  ที่เจอ ทุก key  *****ระวัง ต้องมี key ไม่ใช่การแทรกระหว่างตำแหน่ง เช่น 9 9 9 9 lis1.add_after_node(9,10) ได้ 9->10->9->10->9->10->9->10
        key =str(key)
        data = str(data)
        current = self.head
        while current:
            if current.next is None and current.data == key:
                self.append(data)
                return 
            elif current.data == key:
                new_node = Node(data)
                nxt = current.next #node ถัดจาก node ที่มี data  == key
                current.next = new_node #เพิ่มข้อมูล ใน node ถัดไป 
                new_node.next = nxt #ย้าย node ของ new_node มาที่ current.next (node ล่าสุด)
                new_node.prev = current #ย้าย node ก่อนหน้ามาเป็น head
                nxt.prev = new_node #ให้ ตัวก่อนหน้าเป็น node ล่าสุด
            current = current.next #move to next node

    def add_before_node(self, key, data):
        key =str(key)
        data = str(data)
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.prepend(data)
                return
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                prev.next = new_node 
                current.prev = new_node
                new_node.next = current
                new_node.prev = prev
            current = current.next
    
    def delete(self, key): #ลบ node ที่ต้องการ ***ระวัง ต้องรุ้ค่า key
        key = str(key)
        current =self.head
        while current:
            if current.data == key and current == self.head:
                #Case1
                if not current.next:
                    current = None
                    self.head  = None
                    return
                #Case2
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            elif current.data == key:
                #Case3
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                #Case4
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def delete_node(self, node): #ลบ ข้อมูลซ้ำ (จะมีแค่อย่างละตัว)
        current =self.head
        while current:
            if current == node and current == self.head:
                #Case1
                if not current.next:
                    current = None
                    self.head  = None
                    return
                #Case2
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            elif current == node:
                #Case3
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                #Case4
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next
    
    def reverse(self):
        tmp = None
        current = self.head
        while current:
            tmp = current.prev #node before head
            current.prev = current.next #เลื่อน previous ไปตัวถัดไป
            current.next = tmp #เลื่อน next มา previou
            current = current.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        current = self.head
        seen = dict()
        while current:
            if current.data not in seen:
                seen[current.data] = 1
                current = current.next
            else:
                nxt = current.next 
                self.delete_node(current)
                current = nxt

lis1 = DoubleLinklist()
inp = input("Enter Input :").split()
for i in inp:
    lis1.append(i)


# lis1.add_after_node(9,10)
# lis1.add_before_node(2,15)

# lis1.reverse()
# lis1.delete(6)
lis1.remove_duplicates()
print(lis1.__str__())
            