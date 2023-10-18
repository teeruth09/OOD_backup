'''
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

Enter Your List : -25 -10 -7 -3 2 4 8 10
[[-7, 2, 10], [-7, 4, 8]]

Enter Your List : -3 2 4 6 8 10
[[-3, 2, 6]]

Enter Your List : -100 100
Array Input Length Must More Than 2

Enter Your List : 5 -5 5 -5 5 -5 5 5 -5 -5 -5 -5 5
[[-5, 5, 5]]

'''
# input_value = input("Enter Your List : ")
# values = input_value.split(" ")

# Collection = []
# for value in values:
#     Collection.append(int(value.strip()))

# a,b,c = 0,0,0
# result = []
# for i in Collection:
    
#     '''
#     if a+b+c != 5:
#         a == i 
#         if a == i:
#             result.append(a)
#         elif b == i:
#             result.append(b)
#         elif c == i:
#             result.append(c)
#         print(result)
#     elif a+b+c ==5:
#         print(result)
#     '''

num =input("Enter Your List : ").split()
lst = []
for i in num:
    lst.append(int(i))

print(lst)

target_sum = 5
result = []

for i in range(len(lst)-2):
    for j in range(i+1, len(lst)-1):
        for k in range(j+1, len(lst)):
            if lst[i] + lst[j] + lst[k] == target_sum :
                result.append([lst[i], lst[j], lst[k]])
print(result)
result2 = set(lst)

print(result2)


print(f'Result is :{result2}')

