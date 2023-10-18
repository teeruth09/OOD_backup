'''
<<<  กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก (เดินยังไงให้หลงครับเนี่ยย - -") หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป >>>

****  ด้านบนจะเป็นเนื้อหาของ  < วันหนึ่งฉันเดินเข้าป่า   version  1 >  เผื่อบางคน Random ไม่ได้ครับ


หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :  A  <Heights>  แสดงถึงความสูงของต้นไม้  ,  B  คือการหันหลังกลับมามอง , S  คือการโดนผลกระทบจากเห็ดพิษ

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง


Enter Input : A 4,A 3,B,A 5,A 8,B
2
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B
2
1
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B,S,B
2
1
1
1

Enter Input : A 4,A 3,B,S,B,A 5,A 6,B,S,B
2
1
1
2


Enter Input : S,S,S,B,B,A 6,S,S,S,S,S,S,S,S,B
0
0
1

Enter Input : A 10,A 9,A 8,A 7,B,S,B,A 7,A 1,B,A 50,A 31,S,S,S,S,B
4
2
4
2

Enter Input : A 5,A 4,B,S,S,A 4,B
2
3

Enter Input : A 3,A 4,B,S,S,S,S,S,B
1
2

'''
class Stack:
    def __init__(self):
        self.list = []
        self.height = []
        self.total = 1

    def push(self,value):
        return self.list.append(value)
    
    def push_height(self,value):
        return self.height.append(value)
    
    def pop(self):
        if not self.height:
            return 0
        return self.height.pop()
    

     
    def peek(self):
        if not self.height:
            return 0
        return self.height[-1]



a = input("Enter Input : ").split(",")
s = Stack()

c = 0
def run():
    for i in a:
        s.push(i)
        if i.split()[0] == 'A':
            s.push_height(int(i.split()[1]))
        elif i == 'S':
            new_list = []
            for j in s.height:
                if j % 2 == 0:   #even number
                    j -= 1
                else:      #odd number
                    j += 2
                new_list.append(j)
            s.height = new_list
        elif i == 'B':
            for val in range(0,len(s.height)):
                for nextindex in range(1,len(s.height)):
                    if s.height[val] > s.height[nextindex]:
                        s.total += 1
                        #print(s.total)
                    elif s.height[val] <= s.height[nextindex]:
                        s.total = 1
                        
                        
        
run()

        

    

print(s.list)
print(s.height)