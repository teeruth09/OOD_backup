'''
Doubly
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):#forward
        s = ""
        current =self.head
        while current != None:
            s+= str(current.data)
            current =current.next
            if current is not None:
                s+="->"
        return s
    def isEmpty(self):
        return self.head == None

    def append(self, data):  # Function definition for appending a new node at the tail of the list.
        new_node = Node(data)  # Create a new node with the provided data.
        if self.head == None:  # Check if the linked list is empty (no nodes).
            self.head = new_node  # If it's empty, set both the head and tail to the new node.
            self.tail = new_node
        else:
            new_node.prev = self.tail  # If the list is not empty, set the previous pointer of the new node to the current tail (last node).
            self.tail.next = new_node  # Set the next pointer of the current tail to the new node, linking them.
            self.tail = new_node  # Update the tail to be the new node, making it the new tail.

    def prepend(self, data):  # Function definition for prepending a new node at the head of the list.
        new_node = Node(data)  # Create a new node with the provided data.
        if self.head == None:  # Check if the linked list is empty (no nodes).
            self.head = new_node  # If it's empty, set both the head and tail to the new node.
            self.tail = new_node
        else:
            new_node.next = self.head  # If the list is not empty, set the next pointer of the new node to the current head.
            self.head.prev = new_node  # Set the previous pointer of the current head to the new node, linking them.
            self.head = new_node  # Update the head to be the new node, making it the new head.


    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True
            current = current.next
        return False

    def print_forward(self): #same singly 
        s = ""
        current = self.head
        while current != None:
            s += str(current.data)
            current = current.next
            if current != None:
                s+= "<->"
        return s

    def print_backward(self):
        s = ""
        current = self.tail #last
        while current != None:
            s += str(current.data)
            current = current.prev #move back ward 
            if current != None:
                s+="<->"
        return s

    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        
        if position == 0:
            self.prepend(data)
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current.next is None:  # If we're inserting at the end
            new_node.prev = current
            current.next = new_node
            self.tail = new_node
        else:
            new_node.next = current.next
            new_node.prev = current
            # current.next.prev = new_node
            current.next = new_node
    
    def reverse(self):
        tmp = None
        current = self.head
        while current != None:
            tmp = current.prev
            current.prev = current.next
            current.next = tmp
            current = current.prev
        if tmp:
            self.head = tmp.prev

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)

print("Forward:")
print(dll.print_forward())

print("Backward:")
print(dll.print_backward())

dll.delete(2)
print("After deleting 2:")
print(dll.print_forward())
dll.reverse()
print("After Reverse")
print(dll.print_forward())

