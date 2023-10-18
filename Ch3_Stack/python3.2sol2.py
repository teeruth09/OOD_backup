'''
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

2. วงเล็บปิดเกิน

3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง

Enter expresion : [[)))))
[[))))) Unmatch open-close  


Enter expresion : [[))
[[)) Unmatch open-close

Enter expresion : (())))
(()))) close paren excess

Enter expresion : )}]
)}] close paren excess


Enter expresion : (((
((( open paren excess   3 : (((

Enter expresion : (a+c)(a-b)*c(-a
(a+c)(a-b)*c(-a open paren excess   1 : (

Enter expresion : (([]))
(([])) MATCH

Enter expresion : (){}[]}
(){}[]} close paren excess
'''


class stack:
    def __init__(self) :
        self.value = []
        self.size = 0
    
    def push(self,value) :
        self.value.append(value)
        self.size += 1

    def pop(self) :
        self.size -= 1
        return self.value.pop(-1)

def parenMatching(text):
    s = stack()
    error = 0
    for x in text:
        if x in "{[(":
            s.push(x)
        elif x in ")}]":
            if s.size > 0:
                temp = s.pop()
                # print(temp)
                if not ((temp == "{" and x == "}") or (temp == "(" and x == ")") or (temp == "[" and x == "]")):
                    print(text+" Unmatch open-close")
                    error = 1
                    break
            else :
                print(text+" close paren excess")
                error = 1
                break
    
    if error == 0:
        if s.size>0:
            print(text+" open paren excess   "+str(s.size)+" : "+"".join(s.value))
        else:
            print(text+" MATCH")


text = input("Enter expresion : ")
parenMatching(text) 