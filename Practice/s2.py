class Stack():
    def __init__(self,list= None):
        if list == None:
            self.list = []
        else:
            self.list = list
    
    def push(self,value):
        self.list.append(value)
    
    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)


inp =input("Enter input : ")

s = Stack()

count = 0
error = 0
close = [']',')','}']
for i in inp:
    if s.size() > 0:
        if s.peek() == '{' and i == '}':
            s.pop()
            count +=1
            continue
        elif s.peek() == '[' and i == ']':
            s.pop()
            count +=1
            continue
        elif s.peek() == '(' and i == ')':
            s.pop()
            count +=1
            continue
        for c in close:
            top = s.peek()
            if (top == '[' and (c == i and c != ']')) or (top == '(' and (c == i and c != ')')) or (top == '{' and (c == i and c != '}')):
                error +=1
                break

    if i in '{[(' or '}])':
        s.push(i)


if s.size() == 0:
    print(f'Match {count}')
elif s.size() != 0:
    print(f'Error {error}')