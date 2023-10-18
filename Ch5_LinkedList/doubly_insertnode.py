class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

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

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(3)
dll.insert_at_position(1, 4)
dll.print_forward()
