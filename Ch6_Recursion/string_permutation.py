def permute_string(s, k):
    if k > len(s):
        return 'Invalid value of k. k must be less than or equal to the length of the string.'
    elif k < 0:
        return 'Invalid value of k. k must be a non-negative integer.'
    elif k == 0:
        return '[\'\']'
    else:
        return 1
    
def count(s, c):
    temp = 0
    for i in s:
        if c == i:
            temp += 1
    return temp

def generate_permutation(s, k):
    global string, prev
    if k > 0:
        for i in string:
            if i not in prev:
                prev += i
                generate_permutation(prev, k-1)
            elif i in prev and count(prev, i) < char_count[i]:
                prev += i
                generate_permutation(prev, k-1)
        prev = prev[:-1]   
    else:
        result.append(prev)
        prev = prev[:-1]
        
temp_result = []
result = []
filtered_result = []
index = 0
len_string = 0
temp_k = 0
prev = ''
permuted_s = ''
string = ''
temp_string = string[:]
char_count = dict()

if __name__ == '__main__':
    inp = input('Enter a string and k: ').split('/')
    string = inp[0]
    k = int(inp[1])
    temp_k = k
    len_string = len(string)
    for c in string:
        if c in char_count.keys():
            char_count[c] += 1
        else:
            char_count[c] = 1
    if permute_string(string, k) == 1:
        generate_permutation(string, k)
        for i in result:
            if i not in filtered_result:
                filtered_result.append(i)
        filtered_result.sort()
        print(filtered_result)
    else:
        print(permute_string(string, k))