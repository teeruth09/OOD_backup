'''
Chapter : 9 - item : 5 - Sort Subset
 ส่งมาแล้ว 0 ครั้ง
ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /

1. ด้านซ้าย เป็นผลลัพธ์
2. ด้านขวา เป็น list ของจำนวนเต็ม

โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้

1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก

ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset


****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import

อธิบาย Test Case 1:

[2]
[-1, 3]
[0, 2]  # [-1, 3] กับ [0, 2] มีขนาดเท่ากัน แต่ -1 < 0 ดังนั้น [-1, 3] จึงแสดงผลก่อน [0, 2]
[-3, 2, 3]
[-2, 1, 3]
[-1, 0, 3]
[-1, 1, 2]
[-3, 0, 2, 3]
[-2, -1, 2, 3]
[-2, 0, 1, 3]   # [-2, -1, 2, 3] กับ [-2, 0, 1, 3] มีขนาดและตัวแรกสุดเท่ากัน แต่ตัวที่สอง -1 < 0 ดังนั้น [-2, -1, 2, 3] จึงแสดงผลก่อน [-2, 0, 1, 3]
[-1, 0, 1, 2]
[-3, -1, 1, 2, 3]
[-2, -1, 0, 2, 3]
[-3, -1, 0, 1, 2, 3]



Enter Input : 2/-2 3 1 -1 0 -3 2
[2]
[-1, 3]
[0, 2]
[-3, 2, 3]
[-2, 1, 3]
[-1, 0, 3]
[-1, 1, 2]
[-3, 0, 2, 3]
[-2, -1, 2, 3]
[-2, 0, 1, 3]
[-1, 0, 1, 2]
[-3, -1, 1, 2, 3]
[-2, -1, 0, 2, 3]
[-3, -1, 0, 1, 2, 3]



Enter Input : 2/1 0 2 -1
[2]
[0, 2]
[-1, 1, 2]
[-1, 0, 1, 2]


Enter Input : 3/-1 0 1 2
[1, 2]
[0, 1, 2]


Enter Input : 5/1 2 3 4
[1, 4]
[2, 3]


Enter Input : 4/-1 0 1 2
No Subset
'''

def bubble_sortLength(sublist):
    for loop in range(1, len(sublist)):
        swaped = False
        for i in range(len(sublist) - loop):
            if len(sublist[i]) > len(sublist[i+1]):
                sublist[i], sublist[i+1] = sublist[i+1], sublist[i]
                swaped = True
        if not swaped:
            break
    return sublist

def bubble_sortNum(sublist):
    for loop in range(1, len(sublist)):
        swapped = False

        for i in range(len(sublist) - loop):
            if sublist[i] > sublist[i+1]:
                sublist[i],sublist[i+1] = sublist[i+1],sublist[i]
                swapped = True
        if not swapped:
            break
    return sublist

def sublistSum(target, list, index=0, result=None, carry=None):
    if result is None:
        result = []
    if carry is None:
        carry = []
    if index >= len(list):
        return result
    carry.append(list[index])
    if sum(carry) == target:
        result.append(carry.copy())
    
    result = sublistSum(target, list, index+1, result, carry)
    # print(carry)
    carry.pop()
    result = sublistSum(target, list, index+1, result, carry)
    return result


# Example usage:

inp = input("Enter Input : ").split('/')
target = int(inp[0])
lst = [int(x) for x in inp[1].split()]

sublist= []

lst = bubble_sortNum(lst)
sublist = sublistSum(target, lst)

if len(sublist) != 0:
    for i in bubble_sortLength(sublist):
        print(i)
else:
    print('No Subset')
