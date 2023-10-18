'''
รับข้อความ 2 ข้อความ

ข้อความแรกให้หมุนซ้าย ข้อความที่สองให้หมุนขวา

แสดงผล

หยุดเมื่อข้อความที่หมุน เหมือนข้อความที่รับเข้ามา

โดยแสดงผล 5 บรรทัดแรก และบรรทัดสุดท้าย

*** String Rotation ***
Enter 2 strings : 123 456
1 312 564
2 231 645
3 123 456
Total of  3 rounds.

*** String Rotation ***
Enter 2 strings : dict dept
1 tdic eptd
2 ctdi ptde
3 ictd tdep
4 dict dept
Total of  4 rounds.

*** String Rotation ***
Enter 2 strings : Marvel Stinger
1 lMarve tingerS
2 elMarv ingerSt
3 velMar ngerSti
4 rvelMa gerStin
5 arvelM erSting
 . . . . . 
42 Marvel Stinger
Total of  42 rounds.

print("*** String Rotation ***")
strings = input("Enter 2 strings : "+" ").split()
round = 0

def shift_string(string):
    return string[1:] + string[0]

for i in strings:
    for j in strings[i]:
        a = shift_string(strings[j])
        print(a)
'''

print("*** String Rotation ***")
a, b = [x for x in input("Enter 2 strings : ").split()]
n = len(a)
a_default = a
b_default = b
a1 = a
b1 = b
cnt = 1
a = a[-1] + a[:-1]
print(a)
     
b = b[1:] + b[0]
print(cnt, a, b)
while(a1 != a or b1 != b):
  cnt += 1
  a = a[-1] + a[:-1]
  b = b[1:] + b[0]
  if cnt <= 5:
    print(cnt, a, b)

if cnt > 6:
  print(" . . . . . ")

print(f"Total of  {cnt} rounds.")
