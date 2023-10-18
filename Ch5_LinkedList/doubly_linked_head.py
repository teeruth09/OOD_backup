class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Create a doubly linked list
dll = DoublyLinkedList()

# Append elements to the list
dll.append(1)
dll.append(2)
dll.append(3)

# Display the list
dll.display()
