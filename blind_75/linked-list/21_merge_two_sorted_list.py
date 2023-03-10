
from typing import Optional


class Node:
 
  def __init__(self, val = None, next=None): 
    self.val = val
    self.next = next


class ListNode:
  def __init__(self):  
    self.head = None
    
  
  
  def insert(self, val):
    newNode = Node(val)
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
      print(current.val,end=' ')
      current = current.next
    print()

def buildList(input):
    LL = ListNode()
    for i in range(len(input)):
        LL.insert(input[i])
   
    printLL(LL.head)
    return LL.head
  

def mergeTwoLists( list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result= ListNode()
    head =result
    while(list1 is not None and list2 is not None):
       
        if(list1.val<list2.val):
            result.next=list1
            list1=list1.next
        else:
            result.next=list2
            list2=list2.next
        result=result.next
    
    if(list1 is not None):
        result.next=list1
    else:
        result.next=list2
    
    return head.next
    


printLL(mergeTwoLists(buildList([4,5,12]),buildList([1,10,20])))