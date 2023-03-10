
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
  

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr=head
    length = 0
    
    while curr:
        curr = curr.next
        length += 1
            
    if length == 1 and n == 1:
        return None
    
    elif length == n:
        return head.next

    n=(length-n)-1
    curr=head
   

    while(n>0):
        curr=curr.next    
        n-=1
    
    
    # remove last node
    if(curr.next.next is None):
        curr.next=None
                
    #remove middle node
    else:
        target = curr.next
        curr.next=target.next
        del target
            
            
      
    
    return head
       


printLL(removeNthFromEnd(buildList([1,2,3,4,5]),2))