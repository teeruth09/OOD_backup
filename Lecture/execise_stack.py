i = [x for x in input("a : ").split()]
operator = ['+', '-', '*', '/', 'DUP', 'PSH', 'POP']

for j in i:
    for k in operator:
        if j in k:
            print("true")
        
