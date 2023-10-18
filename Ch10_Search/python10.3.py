'''
Chapter : 10 - item : 3 - Simple Sqrt
 ส่งมาแล้ว 0 ครั้ง
หาค่า Simple-square-root ของจำนวนเต็มบวก x  โดย simple-sqrt คือ จำนวนเต็มที่เมื่อยกกำลังแล้ว จะมีค่าใกล้เคียงหรือเท่ากับ x มากที่สุด

ห้ามใช้ฟังก์ชันช่วยในการหาค่า เช่น sqrt(x), pow(x,0.5) เป็นต้น ให้ใช้ binary-search 

Example 1:
Input:
Enter input: 4

Output:
Simple sqrt: 2

-----------------------------

Example 2:
Input:
Enter input: 8

Output:
Simple sqrt: 2

อธิบาย Example 2:
sqrt(8) = 2.82842...
ดังนั้น ค่าที่ยกกำลังแล้วและเป็นจำนวนเต็ม ที่ใกล้กับ 8 คือ 2


Testcase : #1
simple sqrt: 4
2

Testcase : #2
simple sqrt: 9
3

Testcase : #3
simple sqrt: 8
2

Testcase : #4
simple sqrt: 3
1

'''
#!/usr/bin/python3 

def SquareRootFloor (beg, end, n) :
    
    ans_sqrt = n

    while (beg <= end) :

        mid = int(beg + (end-beg)/2)
        # print ("beg : " + str(beg) + " end : " + str(end) + " mid : " + str(mid))

        if ( mid*mid == n ) : 
            return mid 
        elif ( mid*mid > n) :
            end = mid - 1 
        else :
            # If mid*mid < n, it does not certainly mean that mid is the floor(square_root(n)), it may / may not be.
            # Example n = 15, when mid becomes 2. mid*mid < 15 so 2 could well be the floor(square_root(15)) so store it
            # as the answer and continue the search for a bigger number that could also be the floor(square_root(15))*/
            # print ("Store square root as mid (" + str(mid) + ")")
            ans_sqrt = mid 
            beg = mid + 1 
    
    return ans_sqrt

num = int(input("simple sqrt: "))

print(SquareRootFloor(1,num,num))


# print ("Finding square root of : " + str(num))
# sqrt_n = SquareRootFloor (1, num, num)
# print("Output : "+ str(sqrt_n)+"\n")
