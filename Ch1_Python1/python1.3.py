# เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด
# *** Fun with permute ***
# input : 1,2,3
# Original Cofllection:  [1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

# *** Fun with permute ***
# input : 1,1,2,3
# Original Cofllection:  [1, 1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3], [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]
print("*** Fun with permute ***")
input_value = input("input :"+" ")
values = input_value.split(",")

Collection = []
for value in values:
    Collection.append(int(value.strip()))

#Collection = [int(value.strip()) for value in values]
#Collection.append(int(int1))

print(f'Original Cofllection:  {Collection}')


def permutations(Collection):
    result = []
    generate_permutations(Collection, 0, result)
    result.sort(reverse=True) #เรียงจากมากไปหาน้อย
    return result

def generate_permutations(Collection, start, result):
    if start == len(Collection):
        result.append(Collection.copy())
    else:
        for i in range(start, len(Collection)):
            Collection[start], Collection[i] = Collection[i], Collection[start]
            generate_permutations(Collection, start + 1, result)
            Collection[start], Collection[i] = Collection[i], Collection[start]  # Backtrack
Permutation = permutations(Collection)
print("Collection of distinct numbers:")
print(" "+str(Permutation))

