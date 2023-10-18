class Node : 
    def __init__(self,data,next=None): 
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkStack : 
   
    def __init__(self):
        self.head = None
        self.size = 0
        self.all = []

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def Size(self):
        count = 0
        t = self.head
        while (t):
            count += 1
            t = t.next
        return count

    def push(self, data):
 
        if self.head == None:
            self.head = Node(data)
            self.all.append(Node(data))
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            self.all.append(Node(data))
        self.size += 1
 
    def pop(self):
 
        if self.isEmpty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            self.size -= 1
            return poppednode.data

    def peek(self):
 
        if self.isEmpty():
            return None
        else:
            return self.head.data
        
class LinkQueue:
 
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def Size(self): 
        count = 0
        t = self.front
        while (t):
            count += 1
            t = t.next
        return count

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item)
 
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        self.size += 1

    def DeQueue(self):
 
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if(self.front == None):
            self.rear = None
        return temp

def main(): 
    raw = [e for e in input('Enter Input : ').split(',')]
    stack = LinkStack()
    queue = LinkQueue()
    back = LinkStack()
    for segment in raw : 
        used = segment.split(' ')
        if used[0] == 'E':
            while (not back.isEmpty()):
                back.pop() 
            stack.push(Node(used[1]))
            queue.EnQueue(Node(used[1]))
        elif used[0] == 'B':
            if stack.Size() != 1:
                back.push(stack.pop())
                queue.EnQueue(stack.peek())
                # print(stack.peek())
            else : 
                back.push(stack.pop())
        elif used[0] == 'F':
            if back.Size() >= 1:
                tmp = back.pop()
                stack.push(tmp)
                queue.EnQueue(tmp)
    while (not queue.isEmpty()) :
        print(queue.DeQueue(),end='')
        if queue.size != -1 : 
            print(' -> ',end='')
    print()
    print('BackPath : ',end='')
    while (not stack.isEmpty()) :
        print(stack.pop(),end='')
        if stack.size != 0 : 
            print(' -> ',end='')
    print()
if __name__ == "__main__":
    main()