class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = 0
        self._size = 0
        self.count_loop = 0

    def append(self, item):
        # cur_node = Node(item)
        # if self.head == None:
        #     self.head = cur_node
        # else:
        #     t = self.head
        #     while t.next != None:
        #         t = t.next
        #     t.next = cur_node
        # self._size += 1

        if self.isEmpty():
            self.head = Node(item)
            self._size += 1
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = Node(item)
        self._size += 1

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        str1 = self.head.data
        cur_node = self.head
        i = 0
        while cur_node.next != None:
            if i < self.size():
                str1 += '->'
            cur_node = cur_node.next
            str1 += cur_node.data
            i += 1
        return str1

    def set_next(self, ind1, ind2):
        
        if self.isEmpty():
            return 'Error! {list is empty}'
        if ind1 > self.size() - 1:
            return 'Error! {index not in length}: ' + str(ind1)
        if ind2 > self.size() - 1:
            self.append(str(ind2))
            return 'index not in length, append : ' + str(ind2)

        if ind1 > ind2:
            self.count_loop += 1
            i = 0
            cur_node = self.head
            pre = self.head
            while i < ind1:
                if i < ind2:
                    pre = pre.next
                cur_node = cur_node.next
                #     cur_node = cur_node.next
                # pre = pre.next
                i += 1
            cur_node.next = pre
            return f'Set node.next complete!, index:value = {ind1}:{cur_node.data} -> {ind2}:{pre.data}'

        if ind1 < ind2:
            i = 0
            cur_node = self.head
            pre = self.head
            while i < ind2:
                if i < ind1:
                    cur_node = cur_node.next
                pre = pre.next
                i += 1
            cur_node.next = pre
            return f'Set node.next complete!, index:value = {ind1}:{cur_node.data} -> {ind2}:{pre.data}'

        if ind1 == ind2:
            self.count_loop += 1
            i = 0
            cur_node = self.head
            pre = self.head
            while i < ind1:
                cur_node = cur_node.next
                i+=1
            return f'Set node.next complete!, index:value = {ind1}:{cur_node.data} -> {ind2}:{cur_node.data}'

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0


s = LinkedList()
inp = input('Enter input : ').split(',')
for i in inp:
    if i[0] == 'A':
        s.append(i[2:])
        print(s)
    elif i[0] == 'S':
        print(s.set_next(int(i[2]), int(i[4])))

if s.count_loop > 0:
    print('Found Loop')
else:
    print('No Loop')
    print(s)