'''
Chapter : 10 - item : 4 - Isomorphic string
 ส่งมาแล้ว 0 ครั้ง
วันนี้เป็นวันเกิดพี่ฟง (3 ต.ค.) ดังนั้นพี่จึงจะแจกของขวัญให้น้องๆ
ถ้ากำหนดให้ชื่อน้องๆและชื่อของขวัญแทนด้วยตัวอักษร 1 ตัว
ช่วยหาว่าพี่ฟงจะสามารถให้ของขวัญน้องๆคนละชิ้นโดยที่ไม้ให้ของซ้ำกันได้หรือไม่
รูปแบบ input: str1,str2
Expected Complexity: O(n)
ห้ามใช้ dict set อยากใช้ทำเอง
ตัวอย่าง
รายชื่อน้อง (str1): ACAB
รายชื่อของ (str2): XCXY
เป็น Isomorphic เพราะ A -> X, C -> C, B -> Y
ตัวอย่าง 2
str1: ABAB
str2: XCXY
ไม่เป็น Isomorphic เพราะ A -> X แต่ B -> C และ B -> Y
ตัวอย่าง 3
str1: ACAB
str2: XCXC
ไม่เป็น Isomorphic เพราะ A -> X แต่ C -> C และ B -> C



Enter str1,str2: ACAB,XCXY
ACAB and XCXY are Isomorphic


Enter str1,str2: ABAB,XCXY
ABAB and XCXY are not Isomorphic


Enter str1,str2: ACAB,XCXC
ACAB and XCXC are not Isomorphic


Enter str1,str2: 123456,654321
123456 and 654321 are Isomorphic


Enter str1,str2: y=mx+b,10=5+5
y=mx+b and 10=5+5 are not Isomorphic


Enter str1,str2: y=mx+b,10=4+6
y=mx+b and 10=4+6 are Isomorphic


Enter str1,str2: sanfong,3/10/45
sanfong and 3/10/45 are not Isomorphic

'''
def isomorphic(string1,string2):
    if len(string1) != len(string2):
        return False
    char_map = {}
    seen_chars = set()
    for c1, c2 in zip(string1,string2):
        if c1 not in char_map:
            if c2 in seen_chars:
                return False
            char_map[c1] = c2
            seen_chars.add(c2)
        elif char_map[c1] != c2:
            return False
    return True


inp = input("Enter str1,str2: ").split(',')
str1 = inp[0]
str2 = inp[1]

if isomorphic(str1,str2):
    print(f'{str1} and {str2} are Isomorphic')
else:
    print(f'{str1} and {str2} are not Isomorphic')