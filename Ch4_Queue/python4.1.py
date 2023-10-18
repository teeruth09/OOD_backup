'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

                    หลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***


Enter Input : E 10,E 20,E 30,E 40,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Pop 20 size in queue is 2
Number in Queue is :  ['30', '40']


Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Add 50 index is 3
Add 60 index is 4
Pop 20 size in queue is 4
Pop 30 size in queue is 3
Pop 40 size in queue is 2
Pop 50 size in queue is 1
Pop 60 size in queue is 0
-1
Empty


Enter Input : D,D,D,D,D
-1
-1
-1
-1
-1
Empty


Enter Input : D,E 99,D,D,E 88,D,D,E 12,E 13,E 86
-1
Add 99 index is 0
Pop 99 size in queue is 0
-1
Add 88 index is 0
Pop 88 size in queue is 0
-1
Add 12 index is 0
Add 13 index is 1
Add 86 index is 2
Number in Queue is :  ['12', '13', '86']

'''

class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)
        #return self.list[value]

    def dequeue(self):
        if not self.list:
            return -1
        return f'Pop {self.list.pop(0)} size in queue is {self.size()}'
    
    def bottom(self):
        return self.list[0]
    
    def isEmpty(self):
        if not self.list:
            return f'Empty'
        else:
            return f'Number in Queue is :  {self.list}'

    
    def size(self):
        return len(self.list)
    
que1 = Queue()
a = input("Enter Input : ").split(",")
index = 0

for i in a:
    if i.split()[0] == 'E':
        que1.enqueue(i.split()[1])
        index +=1
        print(f'Add {i.split()[1]} index is {index-1}')

    elif i == 'D':
        pop = que1.dequeue()
        index -= 1
        print(pop)

    if index < 0:
        index = 0

print(que1.isEmpty())