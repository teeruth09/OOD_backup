'''
เขียนภาษา Python เพื่อวาดพีระมิด ซึ่งจะรับ input เป็นขนาดของพีระมิด โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป
*** Fun with Drawing ***
Enter input : 2
#####
#...#
#.#.#
#...#
#####
*** Fun with Drawing ***
Enter input : 5
#################
#...............#
#.#############.#
#.#...........#.#
#.#.#########.#.#
#.#.#.......#.#.#
#.#.#.#####.#.#.#
#.#.#.#...#.#.#.#
#.#.#.#.#.#.#.#.#
#.#.#.#...#.#.#.#
#.#.#.#####.#.#.#
#.#.#.......#.#.#
#.#.#########.#.#
#.#...........#.#
#.#############.#
#...............#
#################
'''
# print("*** Fun with Drawing ***")
# input_value = int(input("Enter input: "))

# # Calculate the size of the pattern
# size = 2 * input_value + 3

# # Draw the pattern
# for row in range(size):
#     for col in range(size):
#         if row == 0 or row == size - 1 or col == 0 or col == size - 1:
#             print("#", end="")
#         elif row == (size - 1) // 2 and col == 1:
#             print(".", end="")
#         elif row == input_value // 2 + 1 and col == size - 2:
#             print(".", end="")
#         elif row == input_value // 2 + 1 and col >= 2 and col <= input_value + 1:
#             print("#", end="")
#         elif row >= 2 and row <= input_value + 1 and col == input_value + 1:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
print("*** Fun with Drawing ***")
input_value = int(input("Enter input: "))

# Calculate the dimensions
width = 2 * input_value + 1
height = input_value * 2 + 1

# Generate the drawing
drawing = ""
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            drawing += "#"
        elif i % 2 == 0:
            drawing += "."
        else:
            if j % 2 == 0:
                drawing += "#"
            else:
                drawing += "."

    drawing += "\n"

print(drawing)



'''
print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
c = 1
y = 4*x-3
if x < 2 :
    print("Error")
else :
    print("#"*y)
    print("#."+"."*(y-4*c)+".#")

    for i in range(y//2-1):
        if(i!=0 and i%2==0):
            c += 1
            print(("#."*c)+"."*(y-4*c)+(".#"*c))
        elif(i!=0 and i%2!=0):
            print(("#."*c)+"#"*(y-4*c)+(".#"*c))

    c+=1

    for i in range(y//2-1,0,-1):
        if(i%2!=0):
            c -= 1
            print(("#."*c)+"#"*(y-4*c)+(".#"*c))
        elif(i!=y//2 and i%2==0):
            print(("#."*c)+"."*(y-4*c)+(".#"*c))

    print("#."+"."*(y-4*c)+".#")
    print("#"*y)
'''



