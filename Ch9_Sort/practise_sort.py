def buble_sort(list):
    for last in range(len(list)-1, 0, -1):
        swap = False
        for i in range(last):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swap = True
        if not swap:
            break

#ต้องทำให้ครบทุกตัวจนกว่าจะครบทุกตัว  Big on = O n^2
def selection(list):
    for last in range(len(list)-1, 0, -1):
        biggest = list[0]
        biggest_i = 0
        for i in range(1, last+1):
            if list[i] > biggest:
                biggest = list[i]
                biggest_i = i 
        #swap element biggest and last eleement
        list[last], list[biggest_i] = list[biggest_i], list[last]



#sort น้อยไปมากเป็นวิธีที่เร็วสุด
# worst case =  o n^2
# best case = o n

def insertionsort(list):
    for i in range(1, len(list)):
        iele = list[i] # inset element

        for j in range(i, -1, -1):
            if iele < list[j-1] and j > 0:
                list[j] = list[j-1] #สลับถ้าน้อยกว่า

            else:
                list[j] = iele
                break 
        

def shell(list, dIncrements):
    for inc in dIncrements: #for each diminishing increment 
        for i in range(inc, len(list)): #insetion sort
            iele = list[i]
            for j in range(i, -1, -inc):
                if iele< list[j-inc] and j >= inc:
                    list[j] = list[j-inc]
                    print(list)
                else:
                    list[j] = iele
                    break

list = [10, 11, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
dincrement = [5, 3, 2, 1]

shell(list, dincrement)
# print(list)



#o n = n log 2 n 
#Merge sort = merge O (n) x d = O (n log  n)

# def merge_sort(list, left, right, rightEnd):
#     start = left 
#     leftEnd = right -1 
#     result = []
#     while left <= leftEnd and right <= rightEnd:
#         if list[left] < list[right]:
#             result.append(list[left])
#             left += 1
#         else:
#             result.append(list[right])
#             right += 1
#     while left <= leftEnd: # copy remaining left half if any
#         result.append(list[left])
#         left += 1
#     while right <= rightEnd: # copy remaining right half if any 
#         result.append(list[right])
#         right += 1
    
#     for ele in result:
#         list[start] = ele
#         start += 1
#         if start > rightEnd:
#             break



def merge_sort(my_list, left, right, rightEnd):
    start = left 
    leftEnd = right - 1 
    result = []
    while left <= leftEnd and right <= rightEnd:
        if my_list[left] < my_list[right]:
            result.append(my_list[left])
            left += 1
        else:
            result.append(my_list[right])
            right += 1
    while left <= leftEnd:
        result.append(my_list[left])
        left += 1
    while right <= rightEnd:
        result.append(my_list[right])
        right += 1

    for ele in result:
        my_list[start] = ele
        start += 1
        if start > rightEnd:
            break

my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list, 0, 2, 6)  # Sort the elements from index 0 to 6
print(my_list)



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr





def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, equal, right = [], [pivot], []

    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    return quick_sort(left) + equal + quick_sort(right)




list = [5, 3, 6, 1, 2, 7, 8, 4]
selection(list)
print(list)