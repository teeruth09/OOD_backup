# จงเขียนโปรแกรมเพื่อรับข้อความ แล้วให้แสดงผล จำนวนตัวอักษรพิมพ์ใหญ่ และ พิมพ์เล็ก และแสดงตัวอักษรที่พบ เรียงตามลำดับตัวอักษร โดยไม่แสดงตัวอักษรซ้ำ 
# และให้แสดงผลตามตัวอย่าง

# หมายเหตุ ให้ระวังตัวอักษรตัวใหญ่ตัวเล็ก ให้ดี

#  *** String count ***
# Enter message : I Love KMITL.
# No. of Upper case characters : 7
# Unique Upper case characters : I  K  L  M  T  
# No. of Lower case Characters : 3
# Unique Lower case characters : e  o  v  

#  *** String count ***
# Enter message : I see the questions in your eyes. I know what's weighing on your mind. You can be sure I know my part.
# No. of Upper case characters : 4
# Unique Upper case characters : I  Y  
# No. of Lower case Characters : 73
# Unique Lower case characters : a  b  c  d  e  g  h  i  k  m  n  o  p  q  r  s  t  u  w  y  

print(" *** String count ***")
message = input()
up_num = 0
low_num = 0
up_character = ""
low_character = ""
up_list = []
low_list = []
for i in range(len(message)):
    #print(message[i])
    for j in message[i]:
        if j.islower():
            low_num +=1
            low_character = j
            #print(low_num)

        if j.isupper():
            up_num +=1
            up_character = j
            #print(up_num)
    up_character = ""
    low_character = ""

print("Enter message :"+" "+message)
print("No. of Upper case characters :"+" "+str(up_num))
print("Unique Upper case characters :"+" "+up_character)