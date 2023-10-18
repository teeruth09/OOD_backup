'''
Chapter : 5 - item : 1 - รู้จักกับ Singly Linked List

ให้เขียนคลาสของ Singly Linked List ซึ่งมีเมท็อดดังนี้
1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
3. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
4. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
5. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
6. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
7. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index 
(0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
8. size           คืนค่าเป็นขนาดของ Linked List
9. pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range

โดยรูปแบบ Input มีดังนี้
1. append    ->  AP
2. addHead  ->  AH
3. search      ->  SE
4. index        ->   ID
5. size          ->   SI
6. pop          ->   PO

โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.head = None
    
    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        else:
            current = self.head 
            s = ""
            while current != None:
                s += str(current.data)
                current = current.next
                if current != None:
                    s += " "
            return s
    
    def isEmpty(self): #isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
        return self.head ==None
    
    def append(self, data): # append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def addHead(self, data): #addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):# search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
        current = self.head
        while current != None:
            if current.data != item:
                current = current.next
            else:
                return "Found"
        else:#last check current.next == None
            return "Not Found"

    def index(self, item):#index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index  (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
        index = 0
        current = self.head
        while current != None:
            if current.data != item:
                current = current.next
                index += 1
            else:
                return index
        else:
            return -1 
        
    def size(self):#size           คืนค่าเป็นขนาดของ Linked List
        current = self.head
        length = 0
        while current != None:
            length +=1
            current = current.next
        return length
        

    def pop(self, pos):#pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
        current = self.head
        index = 0
        if pos == 0 and self.size() != 0: #นำตำแหน่ง index 0 ออก
            if self.size() == 1:
                self.head = None
            elif self.size() > 1:
                self.head = current.next
            return "Success"
        elif pos < 0:
            pass
        elif pos == self.size() -1:
            if self.size() >= 2:
                pass
            while current.next != None:
                current = current.next
            else:
                current = None
                return "Success"
        elif pos >= self.size():
            pass
        else:
            while current != None:
                if index + 1 == pos:
                    current.next = current.next.next
                    return "Success"
                index += 1
        return "Out of Range" 

'''
โดยรูปแบบ Input มีดังนี้
1. append    ->  AP
2. addHead  ->  AH
3. search      ->  SE
4. index        ->   ID
5. size          ->   SI
6. pop          ->   PO
'''
L = SinglyLinkList()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:] , L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
