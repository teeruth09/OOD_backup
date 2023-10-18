class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        current = self.head
        while current:
            s += str(current.data)
            current = current.next
            if current is not None:
                s += " <-> "
        return s

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, key):
        key = str(key)
        current = self.head
        while current:
            if current.data == key and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    self.tail = None
                    return
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            elif current.data == key:
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def delete_node(self, node):
        current = self.head
        while current:
            if current == node and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    self.tail = None
                    return
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            elif current == node:
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
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
            tmp = current.prev
            current.prev = current.next
            current.next = tmp
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
