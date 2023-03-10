
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
    return newNode
  
  

def printLL(head):
    current = head
    while(current):
      print(current.data,end=' ')
      current = current.next
    print()

def buildList(inputs,pos):
    LL = ListNode()
    selectedNode=None
    for i in range(len(inputs)-1):
        node = LL.insert(inputs[i])
        if(i == pos):
           selectedNode=node
    node = LL.insert(inputs[len(inputs)-1])
    node.next= selectedNode

    #printLL(LL.head)
    return LL.head
  

def hasCycle( head: Optional[ListNode]) -> Optional[ListNode]:
    hashMap = {}
    curr=head

    while curr:
       hashMap[curr]=True
       curr=curr.next
       if(curr in hashMap):
          return True
    
    return False


print(hasCycle(buildList([1],-1))) 
