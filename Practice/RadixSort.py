class Queue:
    def __init__(self):
        self.item = []

    def enQueue(self, value):
        self.item.append(value)
        #return self.list[value]

    def deQueue(self):
        if not self.item:
            return -1
        return self.item.pop(0)
    
    def bottom(self):
        return self.item[0]
    
    def isEmpty(self):
        if not self.item:
            return f'Empty'
        else:
            return f'Number in Queue is :  {self.item}'

    
    def size(self):
        return len(self.item)


def radix_sort(l) :
    result = Queue(l)
    max_bits = get_max_digit(max(l))
    qDigit =[Queue(),Queue(),Queue(),Queue(),Queue(),
    Queue(),Queue(),Queue(),Queue(),Queue()]
    for i in range (1,max_bits+1) : 
        while not result.isEmpty() :
            num = result.deQueue()
            num_digit = get_digit(num,i)
            qDigit[num_digit].enQueue(num)
    for i in range (10) :
        while not qDigit[i].isEmpty() :
            result.enQueue(qDigit[i].deQueue())
            return result.item

def get_digit(n, d):
    for i in range(d-1):
        n //= 10
        return n % 10
def get_max_digit(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
        return i
    
