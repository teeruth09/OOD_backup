'''
เขียนภาษา Python เพื่อวาดรูปหยิน-หยาง ซึ่งจะรับ input เป็นขนาดของรูปหยิน-หยาง

Enter Input : 1
..#+++
.##+#+
###+++
###+++
#+#++.
###+..

Enter Input : 2
...#++++
..##+##+
.###+##+
####++++
####++++
#++#+++.
#++#++..
####+...

Enter Input : 3
....#+++++
...##+###+
..###+###+
.####+###+
#####+++++
#####+++++
#+++#++++.
#+++#+++..
#+++#++...
#####+....

Enter Input : 4
.....#++++++
....##+####+
...###+####+
..####+####+
.#####+####+
######++++++
######++++++
#++++#+++++.
#++++#++++..
#++++#+++...
#++++#++....
######+.....

'''
b = 0
n = int(input("enter:"))
for i in range(1,n+1):
    print("e"*n)
    # for j in range(i):
        # print("#",end="")
    print()


# #ก้อนสามเหลี่ยม
# for j in range(n, 0,-1): 
#     for k in range(1, j + 1):
#         print("#",end = "")
#     print('\r') 


# for i in range(1, n+1):
#     spaces = ' '*(n - i)
#     hashes = '#' * i
#     print(spaces + hashes)


# print('*' * n)
# for i in range(n-2):
#     print ('*' + '#' * (n-2) + '*')
# print('*' * n)