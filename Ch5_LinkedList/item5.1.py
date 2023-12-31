'''
สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง 
โดยคลาส LinkedList จะประกอบไปด้วย

1. def __init__(self): สำหรับสร้าง linked list
2. def __str__(self): return string แสดง ค่าใน linked list
3. def isEmpty(self): return list นั้นว่างหรือไม่
4. def append(self, data): เพิ่ม data ต่อท้าย linked list
5. def insert(self, index, data): insert data ใน index ที่กำหนด

โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:s+="->"
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next = p
        self.size+=1
    
    def insert(self, index, data):
        p=Node(data)
        if self.isEmpty():
            self.head = p
        elif index==0:
            p.next = self.head
            self.head = p
        else:
            t=self.head
            i = 0
            while i<index-1:
                i+=1
                t=t.next
            p.next = t.next
            t.next = p
        self.size +=1
        
inp = [i.strip() for i in input("Enter Input : ").split(",")]
l = inp[0].split()
a = LinkedList()
for i in l:a.append(int(i))
if a.isEmpty():
    print("List is empty")
else:
    print("link list : "+a.__str__())
for i in inp[1:]:
    index,data = [int(j)for j in i.split(":")]
    if index<0 or index>a.size:
        print("Data cannot be added")
    else:
        a.insert(index,data)
        print("index = "+str(index)+" and data = "+str(data))
    if a.isEmpty():print("List is empty")
    else:print("link list : "+a.__str__())