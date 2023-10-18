'''
ณ ร้านกาแฟแห่งหนึ่งมีบาริสต้า 2 คน จะมีลูกค้าเข้ามาในร้านเวลา (si) บาริสต้าจะทำกาแฟให้ลูกค้าแต่ละคนในเวลา (pi) ที่ต่างกัน ดังนั้นจะมีคนที่รอคิวอยู่ แสดงลำดับลูกค้าที่ได้กาแฟ และคนที่รอคิวเพื่อจะสั่งกาแฟนานที่สุดรอกี่นาที ถ้าไม่ต้องรอคิวเลยให้แสดง No waiting



ตัวอย่างข้อมูลเข้า

Log : 0,3/0,7/2,3/7,7/10,5/10,1

คำอธิบาย

ลูกค้าคนที่ 1 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 3 นาที 

ลูกค้าคนที่ 2 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 7 นาที 

ลูกค้าคนที่ 3 เข้ามาในเวลาที่ 2 และสั่งกาแฟที่ทำนาน 3 นาที 

ลูกค้าคนที่ 4 เข้ามาในเวลาที่ 7 และสั่งกาแฟที่ทำนาน 7 นาที 

ลูกค้าคนที่ 5 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 5 นาที 

ลูกค้าคนที่ 6 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 1 นาที 



ไทม์ไลน์

เวลา(t)    เหตุการณ์

0    ลูกค้าคนที่ 1 และ 2 เข้ามาในร้านและสั่งกาแฟ

2    ลูกค้าคนที่ 3 เข้ามาในร้าน

3    ลูกค้าคนที่ 1 ได้กาแฟ ลูกค้าคนที่ 3 สั่งกาแฟหลังจากรอคิวไป 1 นาที

6    ลูกค้าคนที่ 3 ได้กาแฟ

7    ลูกค้าคนที่ 2 ได้กาแฟ ลูกค้าคนที่ 4 เข้ามาในร้านและสั่งกาแฟ

10    ลูกค้าคนที่ 5 และ 6 เข้ามาในร้าน ลูกค้าคนที่ 5 สั่งกาแฟ

14    ลูกค้าคนที่ 4 ได้กาแฟ ลูกค้าคนที่ 6 สั่งกาแฟหลังจากรอคิวไป 4 นาที

15    ลูกค้าคนที่ 5 และ 6 ได้กาแฟ



ผลลัพธ์ 

Time 3 customer 1 get coffee  

Time 6 customer 3 get coffee  

Time 7 customer 2 get coffee  

Time 14 customer 4 get coffee  

Time 15 customer 5 get coffee  

Time 15 customer 6 get coffee  

The customer who waited the longest is : 6

The customer waited for 4 minutes

 ***Cafe***
Log : 0,3/0,7/2,3/7,7/10,5/10,1
Time 3 customer 1 get coffee  
Time 6 customer 3 get coffee  
Time 7 customer 2 get coffee  
Time 14 customer 4 get coffee  
Time 15 customer 5 get coffee  
Time 15 customer 6 get coffee  
The customer who waited the longest is : 6
The customer waited for 4 minutes


 ***Cafe***
Log : 0,1/1,1/2,1/3,1/4,1/5,1
Time 1 customer 1 get coffee  
Time 2 customer 2 get coffee  
Time 3 customer 3 get coffee  
Time 4 customer 4 get coffee  
Time 5 customer 5 get coffee  
Time 6 customer 6 get coffee  
No waiting

 ***Cafe***
Log : 0,1/0,1/1,1/1,1/2,1/2,1
Time 1 customer 1 get coffee  
Time 1 customer 2 get coffee  
Time 2 customer 3 get coffee  
Time 2 customer 4 get coffee  
Time 3 customer 5 get coffee  
Time 3 customer 6 get coffee  
No waiting


'''
class Barista:
    def __init__(self):
        self.current_time = 0
        self.time_enque = 0
        self.waiting_time = 0
        self.finish_time = 0 #เวลาที่กาแฟจะเสร็จ
        self.status = True
        self.list_que = []


    def enqueue(self,value):
        return self.list_que.append(value)
    
    def dequeue(self):
        if not self.list_que:
            return 0
        else:
            return self.list_que.pop(0)

    def size(self):
        return len(self.list_que)
        

class Cafe:

    def __init__(self):
        
        self.barista = 2
        self.list_que = []
        self.arrive_time = []
        self.time_per_coffee = []


    def enqueue(self,type_list,value):
        if type_list == self.list_que:
            return type_list.append(value)
        else:
            return type_list.append(int(value))
    
    def dequeue(self):
        if not self.list_que:
            return 0
        else:
            return self.list_que.pop(0)
        
    def size(self):
        return len(self.list_que)


customer = Cafe() 
barista1 = Barista()
barista2 = Barista()

print(" ***Cafe***")
inp = input("Log : ").split("/")

for x in inp:
    customer.enqueue(customer.list_que,x)



for i in range(customer.size()):
    customer.enqueue(customer.arrive_time,customer.list_que[i].split(",")[0])
    customer.enqueue(customer.time_per_coffee,customer.list_que[i].split(",")[1])


timeline = 0

for x in customer.list_que:

    
      
        if barista1.size() == 0:
            barista1.enqueue(x)
            #print(x)
            barista1.finish_time = barista1.finish_time + int(x.split(",")[1])
            print("barista 1 fin :",barista1.finish_time)
        elif barista2.size() == 0:
            barista2.enqueue(x)
            barista2.finish_time = barista2.finish_time + int(x.split(",")[1])
            print("barista 2 fin :",barista2.finish_time)
        elif barista1.finish_time <= barista2.finish_time and barista1.size() != 0:
            a = barista1.enqueue(x)
            #print(x)
            barista1.time_enque = int(x.split(",")[0])
            #print(barista1.time_enque)
        elif barista1.finish_time > barista2.finish_time and barista2.size() != 0: 
            barista2.enqueue(x)
            barista2.time_enque = int(x.split(",")[0])


        # if barista1.finish_time > barista2.finish_time:
        #     timeline = barista1.finish_time
        # else:
        #     timeline = barista2.finish_time
# ... Your previous code ...
longest_wait_time = 0
while customer.size() > 0 or barista1.size() > 0 or barista2.size() > 0:
    next_customer = None

    # Check if there are customers arriving at the current timeline
    while customer.size() > 0 and int(customer.list_que[0].split(",")[0]) <= timeline:
        current_customer = customer.dequeue()
        next_customer = current_customer

        # Choose the barista with the earlier finish time
        if barista1.finish_time <= barista2.finish_time:
            barista1.enqueue(current_customer)
            finish_time = max(timeline, int(current_customer.split(",")[0])) + int(current_customer.split(",")[1])
            barista1.finish_time = finish_time
            wait_time = max(0, timeline - int(current_customer.split(",")[0]))
        else:
            barista2.enqueue(current_customer)
            finish_time = max(timeline, int(current_customer.split(",")[0])) + int(current_customer.split(",")[1])
            barista2.finish_time = finish_time
            wait_time = max(0, timeline - int(current_customer.split(",")[0]))

        longest_wait_time = max(longest_wait_time, wait_time)

    # Dequeue from Barista1 if its finish time is equal to the current timeline
    if barista1.size() > 0 and barista1.finish_time == timeline:
        served_customer = barista1.dequeue()
        print(f"Time {timeline}: Customer {served_customer} gets coffee")
        next_customer = served_customer

    # Dequeue from Barista2 if its finish time is equal to the current timeline
    if barista2.size() > 0 and barista2.finish_time == timeline:
        served_customer = barista2.dequeue()
        print(f"Time {timeline}: Customer {served_customer} gets coffee")
        next_customer = served_customer

    if next_customer:
        timeline = max(timeline, int(next_customer.split(",")[0]))

    timeline += 1

print(f"The customer who waited the longest is: {longest_wait_time}")



   
        


print(barista1.list_que)

        

   

