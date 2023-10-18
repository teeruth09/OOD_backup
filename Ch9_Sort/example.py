#bubble sort
def bubble_sort(l):
    for last in range(len(l)-1, 0, -1): #จาก last index to index 0
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1], l[i] #swap
                swaped = True
        if not swaped:
            break
    return l

#selection sort 
def selection_sort(l):
    for last in range(len(l)-1, 0, -1):#จาก last index to index 0
        biggest = l[0]
        biggest_index = 0 #ตำแหน่ง ของค่าใหญ่สุด
        for i in range(1, last+1):#จากตำปหน่ง 1 ถึง last หาค่าใหญ่สุด
            if l[i] > biggest:
                biggest = l[i]
                biggest_index = i
            #swap elements biggest and last element 
        l[last],l[biggest_index] = l[biggest_index], l[last]
    
    return l

#insertion sort 
def insertion_sort(l):
    for i in range(1,len(l)): #from index 1 to last index
        iEle = l[i]  #insert element
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j >0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
    return l


#shell sort (Donald Shell)
def shell(l, dIncrements):
    for inc in dIncrements: #for each diminishing increment 
        for i in range(inc, len(l)): #inseertion sort 
            iEle = l[i]
            for j in range(i, -1, -inc):
                if iEle < l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break
        

#quick sort 
def quick(l, left,right):
    if left == right+1 :#only 2 element
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left] #swap
        return
    if left<right:
        #partition 
        pivot = l[left] #first element pivot
        i, j = left+1, right 
        while i<j:
            while i<right and l[i] <= pivot:
                i +=1
            while j>left and l[j] >= pivot:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i] #swap
        if left is not j:
            l[left], l[j] = l[j],pivot #swap pivot to index j
        quick(l, left, j-1)
        quick(l, j+1,right)
    return l


l = [1,5,2,3,4,6,8]

print(f'bubble sort : {bubble_sort(l)}')

print(f'selection sort : {selection_sort(l)}')

print(f'insertion sort : {insertion_sort(l)}')

print(f'quick sort : {quick(l,0,len(l)-1)}')