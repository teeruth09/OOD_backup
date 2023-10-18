class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinklist:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        s = ""
        current = self.head
        while current != None:
            s += str(current.data)
            current = current.next
            if current != None:
                s += "->"
        return s

    def isEmpty(self):
        return self.head == None
   
    def append(self, data): #add tail
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def add_head(self, data):  #add head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_node(self, index, data):
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

    def search(self, item):
        current =self.head 
        while current != None:
            if current.data == item:
                return "Found"
            current = current.next
        else:
            return "Not Found"

    def index_search(self, item):
        index = 0
        current =self.head 
        while current != None:
            if current.data == item:
                return index
            current = current.next
            index += 1 
        else:
            return "Not Foun item"
    
    def search_data_in_index(self, index):
        current= self.head
        i=0
        if index > self.size():
            return "out of range"
        else:
            while i<index:
                current = current.next
                i += 1
            return current.data

    def size(self):
        length = 0
        current = self.head
        while current != None:
            length+=1
            current = current.next
        return length
    
    def dequeue(self):#delete first 
        if self.isEmpty():
            return "head is None"
        else:        
            self.head = self.head.next

    def pop(self):#เอาตัวท้ายออก
        current = self.head
        while current.next.next != None:
            current = current.next
        current.next = None
        return current.data

    def reverse(self):
        prev = None
        current = self.head
        next = self.head.next
        while current != None:
            next = current.next
            current.next = prev
            prev = current 
            current = next
        self.head = prev
        return self.head.data
               
    
    
list = SinglyLinklist()
inp = input("Enter input : ").split()
for i in inp:
    list.append(i)
print(list.__str__())
list.add_head(5)
print(list.__str__())
list.insert_node(1,20)
print(list.__str__())

list.insert_node(0,15)
print(list.__str__())

index =5
print(f'in index {index} is {list.search_data_in_index(index)} ')
list.dequeue()
print(list.__str__())
print(list.pop())
print(list.__str__())
list.reverse()
print(list.__str__())

