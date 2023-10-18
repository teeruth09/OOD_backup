'''
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())


* Stack Calculator *
Enter arguments : 5 6 +
11

* Stack Calculator *
Enter arguments : 3 DUP +
6

* Stack Calculator *
Enter arguments : 6 5 5 7 * - /
5

* Stack Calculator *
Enter arguments : a b c +
Invalid instruction: a

* Stack Calculator *
Enter arguments : 12
12

* Stack Calculator *
Enter arguments : 9 14 DUP + - 3 POP
19


* Stack Calculator *
Enter arguments : 1 2 3 4 5 POP POP POP
2

* Stack Calculator *
Enter arguments : 4 POP
0

'''

class Stack:
    def __init__(self):
        self.__stack = []

    def __repr__(self):
        temp = [str(e) for e in self.__stack[::]]
        return '[' + ','.join(temp) + ']'

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        if not self.__stack:
            return 0
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

    def isEmpty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)

    def peek(self):
        if not self.__stack:
            return 0
        return self.__stack[-1]


class StackCalc:
    def __init__(self):
        self.OPERATOR = ['+', '-', '*', '/', 'DUP', 'PSH', 'POP']
        self.val = 0
        self.stack = Stack()

    def run(self, expr):
        for val in expr:
            if val.isnumeric():              #check is val = 0-9
                self.stack.push(val)
            elif val not in self.OPERATOR:
                self.val = f"Invalid instruction: {val}"
                return
            else:
                if val in '+-*/':
                    a = self.stack.pop()
                    b = self.stack.pop()
                    operator = val
                    infix = a + operator + b
                    self.stack.push(str(int(eval(infix))))
                else:
                    if val == 'DUP':
                        self.stack.push(self.stack.peek())
                    elif val == 'PSH':
                        pass
                    elif val == 'POP':
                        self.stack.pop()
            self.val = self.stack.peek()

    def getValue(self):
        return self.val


print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())