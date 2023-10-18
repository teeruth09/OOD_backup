'''
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง

Enter Input (L1,L2) : 1 2
L1    : 1 
L2    : 2 
Merge : 1 2 

Enter Input (L1,L2) : 1->2->3 4->5
L1    : 1 2 3 
L2    : 4 5 
Merge : 1 2 3 5 4

Enter Input (L1,L2) : I->Love->KMITL Datastruct->and
L1    : I Love KMITL 
L2    : Datastruct and 
Merge : I Love KMITL and Datastruct

Enter Input (L1,L2) : CE->2D Lardkrabang->KMITL
L1    : CE 2D 
L2    : Lardkrabang KMITL 
Merge : CE 2D KMITL Lardkrabang

'''


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def __str__(self):
    if self.isEmpty():
      return "Empty"
    cur, s = self.head, str(self.head.value) + " "
    while cur.next is not None:
      s += str(cur.next.value) + " "
      cur = cur.next
    return s

  def isEmpty(self):
    return self.head is None

  def append(self, item):
    new_node = Node(item)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next is not None:
        cur = cur.next
      cur.next = new_node

  def addHead(self, item):
    new_node = Node(item)
    new_node.next = self.head
    self.head = new_node

  def search(self, item):
    cur = self.head
    while cur is not None:
      if cur.value == item:
        return "Found"
      cur = cur.next
    return "Not Found"

  def index(self, item):
    cur = self.head
    idx = 0
    while cur is not None:
      if cur.value == item:
        return idx
      cur = cur.next
      idx += 1
    return -1

  def size(self):
    size = 0
    cur = self.head
    while cur is not None:
      cur = cur.next
      size += 1
    return size

  def pop(self, pos):
    if self.isEmpty() or pos < 0 or pos >= self.size():
      return "Out of Range"

    if pos == 0:
      removed_value = self.head.value
      self.head = self.head.next
    else:
      prev = None
      cur = self.head
      count = 0
      while cur is not None and count < pos:
        prev = cur
        cur = cur.next
        count += 1
      removed_value = cur.value
      prev.next = cur.next

    return "Success"

  def reverse(self):
    prev = None
    cur = self.head
    while cur is not None:
      next_node = cur.next
      cur.next = prev
      prev = cur
      cur = next_node
    self.head = prev


def merge_linked_lists(list1, list2):
  list2.reverse()

  cur = list1.head
  while cur.next is not None:
    cur = cur.next

  cur.next = list2.head
  return list1


if __name__ == '__main__':
  l1, l2 = input("Enter Input (L1,L2) : ").split()
  linked_list_1 = LinkedList()
  linked_list_2 = LinkedList()
  for i in l1.split("->"):
    linked_list_1.append(i)

  for i in l2.split("->"):
    linked_list_2.append(i)

  print(f"L1    : {linked_list_1}")
  print(f"L2    : {linked_list_2}")

  print(f"Merge : {merge_linked_lists(linked_list_1, linked_list_2)}")