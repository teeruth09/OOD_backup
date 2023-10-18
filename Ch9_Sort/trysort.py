def bubble_sort(list):
    for last in range(len(list)-1, 0, -1):
        swap = False
        for i in range(last):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swap = True
        if not swap:
            break

