'''
พี่บ่าวสงสัยหลักการทำงานของการ forward และ backward ของ browser เลยไปทำการศึกษามาปรากฎว่ามันใช้หลักการของ linkedlist ซึ่งบังเอิญตรงกับเนื้อหาที่น้องๆ 2D กำลังศึกษาอยู่พอดี พี่เลยอยากให้น้องๆรู้ว่าจริงๆแล้ว linkedlist นั้นมีประโยชน์มากๆเลย โดยหลักการทำงานมันมีอยู่ว่าหากเราเข้า a.com แล้วไป b.com ต่อและอยากกลับมาหน้าเดิมก็กดปุ่ม backward ก็จะกลับมาที่ a.com และหากเข้า c.com แล้วย้อนกลับมา ก็จะกลับมาได้แค่ a.com ไม่ว่าเราจะย้อนสักกี่ครั้ง b ก็ไม่กลับมา

"ก็เหมือนกับแก้วที่แตกไปแล้ว ก็ต้องซื้อใหม่ ต่อให้เป็น Nasa ก็พาเธอกลับมาไม่ได้เธอไปนอกใจ ไม่ได้ไปนอกโลก"

Example

Enter Input : E google.com,E facebook.com,B,E youtube.com,B,F

History : google.com -> facebook.com -> google.com -> youtube.com-> google.com -> youtube.com

BackPath : youtube.com -> google.com

Description

E -> เข้า URL นั้นๆ จะตามด้วย URL เสมอ

B -> Backward ย้อนกลับมา 1 ครั้งเสมอ

F -> Forward ไปข้างหน้า 1 ครั้งเสมอ

History ให้แสดงว่าเคยเข้า URL ไหนไปบ้าง

BackPath ให้แสดง hierarchy ของ Path ที่เราสามารถย้อนกลับไปได้โดยให้แสดงจาก current มา first

ปล. โดยทุกการเข้า URL จะเริ่มที่หน้า welcome ของ browser เสมอ แต่ไม่ต้องนำไปใส่ใน history หรือ backpath ดูตัวอย่างได้ที่ TestCase 2


Enter Input : E bxdman.com,E google.com,E facebook.com,B,E ce-isag.com
History : bxdman.com -> google.com -> facebook.com -> google.com -> ce-isag.com
BackPath : ce-isag.com -> google.com -> bxdman.com

Enter Input : E google.com,E facebook.com,B,E youtube.com,B,F
History : google.com -> facebook.com -> google.com -> youtube.com -> google.com -> youtube.com
BackPath : youtube.com -> google.com

Enter Input : E php.net,E book.hacktricks.xyz,E portswigger.net,B,E google.com,E kali.org,B,F
History : php.net -> book.hacktricks.xyz -> portswigger.net -> book.hacktricks.xyz -> google.com -> kali.org -> google.com -> kali.org
BackPath : kali.org -> google.com -> book.hacktricks.xyz -> php.net

'''


class Node :
    def __init__(self,data,next=None , prev=None):
        self.data = data
        if next :
            self.next = next
        else :
            self.next = None
        if prev :
            self.prev = prev
        else :
            self.prev = None
    def __str__(self) -> str:
        return f'{self.data}'
    
class Queue :
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        self.items.pop(0)
    def __str__(self) -> str:
        return ' -> '.join([str(x) for x in self.items])


             
inp = input("Enter Input : ").split(",")


q = Queue()
position = None
status_back = False
status_forward = False


for section in inp :
    try :
        action , data  = section.split(" ")
    except :
        action = section
    if action == "E" :
        n = Node(data)
        if not position  :
           position = n
           web = Node("welcome.com")
           n.prev  = web
        else :
            position.next = n
            n.prev = position
            position = n
        q.enqueue(position)
    elif action == "B" :
        if position.prev and position:
            # if position.next :
            #     position.next = None
            status_back = True
            position = position.prev
            if position.data == "welcome.com" :
                continue
            q.enqueue(position)
    elif action == "F":
        if position and position.next :
            # if position.prev :
            #     position.prev = None
            position = position.next
            q.enqueue(position)
print("History :",q)
s = []
while position :
    if position.prev and position:
            if position.data == "welcome.com" :
                continue
            s.append(position.data)
            if position.next :
                position.next = None
            
            position = position.prev
            
    else :
        if position.data == "welcome.com" :
                break
        s.append(position.data)
        break
print( "BackPath :", " -> ".join(s))