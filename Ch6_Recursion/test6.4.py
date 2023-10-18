'''
Grouping 

แบ่งกลุ่ม  character โดยบอกว่า Character ตรง ตำแหน่งที่ Pin คือตัวอะไรและกลุ่มนั้นมีจำนวนเท่าไหร่

หากไม่มี String ให้แสดง Output : List is entry

หาก pin ที่ใส่มามากกว่าขนาดของ String ให้แสดง Output : Pin number out of range

หาก pin น้อยกว่า 1 ให้แสดง  Output : Pin number less than 1

******** ห้ามใช้ For / While ********

input : string,pin

Ex : 111112211002111,2

         string = 111112211002111

         pin = 2

               = 1(1)1112211002111 

         จำนวนในกลุ่ม = [11111],[22],[11],[00],[2],[111] = 5

******* Output *******

Character : 1

Count : 5



input number : 123456789,3
Character : 3
Count : 1


input number : abccasssdacccsd,4
Character : c
Count : 2

input number : ,1
Output : List is entry

input number : 12345,10
Output : Pin number out of range

input number : abc,0
Output : Pin number less than 1

input number : 1111111111111111111111111111111111111,10
Character : 1
Count : 37

'''
def count_group(st, index, min, max, target):
    if index>max or index<min or st[index]!=target:
        return 0
    left = count_group(st, index-1, min, index-1, target)
    right = count_group(st, index+1, index+1, max, target)
    return 1+left+right
def solve(st, pos):
    if not st:
        print("Output : List is entry")
        return
    if pos>len(st):
        print("Output : Pin number out of range")
        return 
    if pos<1:
        print("Output : Pin number less than 1")
        return
    print(f"Character : {st[pos-1]}")
    print(f"Count : {count_group(st, pos-1, 0, len(st)-1, st[pos-1])}")
    
    
inp = input("input number : ")
solve(inp.split(",")[0], int(inp.split(",")[1]))