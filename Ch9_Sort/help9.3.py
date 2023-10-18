'''
insertion sort [recursive]
'''
def find_index(l: list, i: int, end: int) -> int:
    if i < 0 or l[i] < end:
        return i
    l[i+1] = l[i]
    return find_index(l, i-1, end)

def insertion_sort(l: list, n: int ) -> None:
    if n <= 1:
        return
    insertion_sort(l, n-1) 
    end = l[n-1]   
    i = find_index(l, n-2, end)
    l[i+1] = end 
    print(f'insert {end} at index {i+1} : ',end='')
    print(f'{l}' if len(l) == n else f'{l[:n]} {l[n:]}')

def main():
    inp = list(map(int, input("Enter Input : ").split()))
    insertion_sort(inp,len(inp)) or print(f'sorted\n{inp}')

if __name__ == '__main__':
    main()