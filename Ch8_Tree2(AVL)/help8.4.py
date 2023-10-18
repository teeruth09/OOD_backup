'''
Mondstadt
'''
class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class Tree:
    def __init__(self): 
        self.root = None
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

def insert_subtree(r,num,val):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1)-1
        current = r
        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val)
            return
        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val)
            return
        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val)
        else:
            insert_subtree(current.right,num - pow(2,h),val)
    else:
        return

def height(root):
    if root == None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left>right:
            return left + 1
        else:
            return right + 1

def sum_root(root: Tree) -> Tree:
    return root.data + sum_root(root.left) + sum_root(root.right) if root else 0

def find_root(root: Tree,i: int) -> Tree:
    j = 0
    if not root:
        return
    l = [root]
    while l:
        cur = l.pop(0)
        if j == i:
            break
        if cur.left:
            l.append(cur.left)
        if cur.right:
            l.append(cur.right)
        j+=1
    return cur

def get_operator(root: Tree,t1: int, t2: int) -> str:
    res = sum_root(find_root(root,t1)) - sum_root(find_root(root,t2))
    return "<" if res<0 else ">" if res>0 else "="

def main():
    T = Tree()
    kn,vs = input("Enter Input : ").split('/')
    for i in kn.split():
        T.insert(int(i))
    print(sum_root(T.root))
    for i in vs.split(','):
        t1,t2 = i.split()
        print(f"{t1}{get_operator(T.root,int(t1),int(t2))}{t2}")
      
if __name__ == '__main__':
    main()