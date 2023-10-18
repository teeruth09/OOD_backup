'''
โจทย์: การเรียงข้อมูลเข้าแถว
คำอธิบาย: รับข้อมูลตัวเลขเข้ามา แล้วนำมาเรียงในแถวเลขตามลำดับ

Input: 5, 3, 1, 4, 2
Output: 1, 2, 3, 4,
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
        
    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def sort_stack(self):
        temp_stack = Stack()
        while not self.is_empty():
            current = self.pop()

            while (not temp_stack.is_empty()) and (temp_stack.peek() > current):
                self.push(temp_stack.pop())

            temp_stack.push(current)

        # Reverse the sorted elements to get them in ascending order
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        return self.items

# Example usage:
input_list = [5, 3, 1, 4, 2]
stack = Stack()
for num in input_list:
    stack.push(num)

sorted_list = stack.sort_stack()
print(sorted_list)  # Output: [1, 2, 3, 4, 5]

            
            

    