'''
เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด
*** Fun with permute ***
input : 1,2,3
Original Cofllection:  [1, 2, 3]
Collection of distinct numbers:
 [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

*** Fun with permute ***
input : 1,1,2,3
Original Cofllection:  [1, 1, 2, 3]
Collection of distinct numbers:
 [[3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3], [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]

'''
def n(l):
    present = l.copy()                                                    #copy current list
    answer.append(present)                                                #append present list 
    Q = l.copy()
    for j in range(0, len(l)-1):                                          #list start at 0
        q = Q[j]
        Q[j] = Q[j+1]
        Q[j+1] = q
        C = Q.copy()
        answer.append(C)
        
def set(l):
    temp = l.copy()                                                   #copy current list
    n(temp)                                                           #do function one round
    for i in range(1, len(l)-1):
        for j in range(1, len(l)-1):
            q = temp[j]
            temp[j] = temp[j+1]
            temp[j+1] = q
            #print(temp)
            n(temp)
        #print("break")
        #print(f'test1{temp}')
        q = temp[1]
        temp[1] = temp[len(l)-1]
        temp[len(l)-1] = q
        #print(f'test2{temp}')
        if i != len(l)-2:
            #print(i)
            #print(f'test3{temp}')
            n(temp)


Collection = []
answer = []
print("*** Fun with permute ***")

i = input("input : ")
num = i.split(",")
for value in num:
    Collection.append(int(value.strip()))
input_value = [int(j) for j in input("input : ").split(",")]
print(f'Original Cofllection:  {input_value}')
xx = input_value[::-1]
yy = Collection[::-1]
set(xx)
set(yy)
print(f'Collection of distinct numbers:\n {answer}')
if set(xx) == set(yy):
    print("True")

        
        




'''
print("*** Fun with permute ***")
myList = list(map(int , input("input : ").split(','))) #input("input: ")
print("Original Cofllection: ", myList)
myList = myList[::-1]
print("Collection of distinct numbers:")
print(' ', end = '')

def addperm(posi,l):
    return [ l[0:i] + [myList[posi]] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]

print(perm([ i for i in range(len(myList))]))
'''