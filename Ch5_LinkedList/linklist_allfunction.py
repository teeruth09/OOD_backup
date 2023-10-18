'''
Singly 
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

    def insert_node(self, index, data): #insert node ใดๆ
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(int(index)-1):
                if current.next != None:
                    current = current.next
            new_node.next = current.next
            current.next = new_node

    

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
        

    def pop(self, pos):#pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range  remove node ใดๆ
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
    
    def reverse(self): # Reverse the linked list
        prev = None         # Initialize a variable `prev` to keep track of the previous node (starts as None)
        current = self.head # Initialize a variable `current` to point to the current node, starting from the head
        next = self.head.next  # Initialize a variable `next` to point to the next node (the one after `current`)

        while current is not None:  # Start a loop that runs until `current` reaches the end of the list (None)
            next = current.next    # Store a reference to the next node in the `next` variable
            current.next = prev    # Reverse the link of the current node to point to the previous node

            prev = current         # Move `prev` to the current node (for the next iteration)
            current = next         # Move `current` to the next node (for the next iteration)

        self.head = prev          # After the loop, update the head to the last node (which is now the first node in the reversed list)
        return self.head.data    # Return the data of the new head (previously the last node)

    


list = SinglyLinkList()

inp = input("Enter Input : ").split()

for i in inp:
    list.append(i)
print(f'Start : {list.__str__()}')

list.addHead(10)
print(f'After add Head : {list.__str__()}')
print(f'list.size = {list.size()}')

index = 2
list.insert_node(index,20)
print(f'After Insert at index {index} : {list.__str__()}')
print(f'list.size = {list.size()}')

pos = 0

print(f'*{list.pop(pos)}* ----> list After Pop index {pos} is {list.__str__()}')
print(f'list.size = {list.size()}')

item = '1'
print(f'Search -> {list.search(item)}')
print(f'Index -> {list.index(item)}')



print(f'Use reverse function Now head is {list.reverse()}')
print(f'list After reverse : {list.__str__()}')

print("**********************")
print(f'Search -> {list.search(item)}')
print(f'Index -> {list.index(item)}')

