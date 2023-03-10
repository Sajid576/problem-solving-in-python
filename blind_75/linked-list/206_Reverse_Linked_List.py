
from typing import Optional


class Node:
 
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next


class ListNode:
  def __init__(self):  
    self.head = None
    self.head = None
  
  
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  

def printLL(head):
    current = head
    while(current):
      print(current.data,end=' ')
      current = current.next
    print()

def buildList(input):
    LL = ListNode()
    for i in range(len(input)):
        LL.insert(input[i])
   
    printLL(LL.head)
    return LL.head
  

def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    return prev


reversedHead = reverseList(buildList([1,2,3,4,5]))
printLL(reversedHead)