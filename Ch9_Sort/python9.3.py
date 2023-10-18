'''
Chapter : 9 - item : 3 - insertion sort [recursive]
 ส่งมาแล้ว 0 ครั้ง
เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***


Enter Input : 1 2 3 4
insert 2 at index 1 : [1, 2] [3, 4]
insert 3 at index 2 : [1, 2, 3] [4]
insert 4 at index 3 : [1, 2, 3, 4] 
sorted
[1, 2, 3, 4]


Enter Input : 1 3 4 2
insert 3 at index 1 : [1, 3] [4, 2]
insert 4 at index 2 : [1, 3, 4] [2]
insert 2 at index 1 : [1, 2, 3, 4] 
sorted
[1, 2, 3, 4]


'''
#insertion sort 
def insertion_sort(l):
    for i in range(1,len(l)): #from index 1 to last index
        iEle = l[i]  #insert element
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j >0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                
                break
    # print(j)
    return l,j


#insertion sort recursive
def insertion_sort_recursive(list1,list2):
    a = list2.pop(0)
    list1.append(a)
    index = insertion_sort(list1)[1]
    if len(list2) > 0:
        print(f'insert {a} at index {index} : {list1} {list2}')
    else:
        print(f'insert {a} at index {index} : {list1}')
        print("sorted")
        print(list1)
    if len(list2) > 0:
        return insertion_sort_recursive(list1,list2)    
    

inp = input("Enter Input : ").split()
data = [int(x) for x in inp]
list1 = [data[0]]
list2 = data[1:]

insertion_sort_recursive(list1,list2)