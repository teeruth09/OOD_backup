'''
Tail Recursion
'''


def fibR(n):
    if n <= 1:
         return n 
    else:
         return fibR(n-1) + fibR(n-2)

print(fibR(5))