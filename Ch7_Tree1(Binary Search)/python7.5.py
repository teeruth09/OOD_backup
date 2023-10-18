'''
Chapter : 7 - item : 5 - Pretty Tree

ปริ้นต้นไม้ BST เป็นแนวนอน          ที่ครูสอนพี่ฟงนั้นขัดใจ
อยากให้น้องทำใหม่ช่วยแก้ไข        ให้ต้นไม้ตั้งตรงแตกกิ่งได้
เลขวรรคขั้นสำหรับข้อมูลรับ            แนะว่านับจำนวนให้ดีไว้
ทำออกมาให้สวยงามประทับใจ       กฤษฎาอยู่ในป่ายังเชยชม

*วนลูป insert เลขทีละตัวเข้า tree ตามปกติ < อยู่ซ้าย, >= อยู่ขวา


Enter input: -1
-1

Enter input: -1 -2
   -1
  /  
-2   


Enter input: -2 -2
-2   
  \  
   -2

Enter input: 1 2 3 4 5
1        
 \       
  2      
   \     
    3    
     \   
      4  
       \ 
        5


Enter input: 5 4 3 2 1
        5
       / 
      4  
     /   
    3    
   /     
  2      
 /       
1

Enter input: 3 2 1 4 5
    3    
   / \   
  2   4  
 /     \ 
1       5

Enter input: 4 5 3 1 2
      4  
     / \ 
    3   5
 __/     
1        
 \       
  2   


Enter input: 100 120 110 110 130 90 60 70 75 74 76
                  100                
                 /   \________       
               90             120    
  ____________/          ____/   \   
60                    110         130
  \                      \           
   70                     110        
     \___                            
         75                          
        /  \                         
      74    76  


Enter input: -100 -120 -110 -110 -130 -90 -60 -70 -75 -74 -76
                    -100                        
         __________/    \                       
     -120                -90                    
    /    \                  \________________   
-130      -110                               -60
              \                             /   
               -110                      -70    
                                    ____/       
                                 -75            
                                /   \           
                             -76     -74        


Enter input: 1 3 2 5 4 6 7 9 8 11 13 12 10 15 14
1                                  
 \__                               
    3                              
   / \__                           
  2     5                          
       / \                         
      4   6                        
           \                       
            7                      
             \__                   
                9                  
               / \___              
              8      11            
                    /  \___        
                  10       13      
                          /  \___  
                        12       15
                                /  
                              14


'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self.insert_helper(self.root,data)
    
    def insert_helper(self, node, data):
        if node is None:
              node = Node(data)
        elif data < node.data:
              node.left = self.insert_helper(node.left, data)
        elif data > node.data:
              node.right = self.insert_helper(node.right, data)
        return node
    
    def print_tree(self):
        self.print_tree_help(self.root, 0)
    
    def print_tree_help(self, node, indent):
        if node:
          pass



bst = BST()
inp = [int(x) for x in input("Enter input: ").split()]

for i in inp:
    bst.insert(i)


bst.print_tree()

