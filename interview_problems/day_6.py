
class Node:
        def __init__(self,data):
            self.data=data
            #self.xnode=xnode            #stores the XOR of prev and next node

def doXOR(node1,node2):
        xnp=node1^node2
        print(str(xnp))

class XORLinkList:
        def __init__(self):
            self.headval = None

list1=XORLinkList()
node1=Node(2)
node2=Node(4)
xnp=doXOR(node1,node2)
print(xnp)