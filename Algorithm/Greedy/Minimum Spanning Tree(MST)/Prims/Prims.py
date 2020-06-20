from collections import defaultdict
import bisect

# Using a Python dictionary to act as an adjacency list
# startingNode--> (destinationNode,weight)

graph = {
     1 : [(2,3)],
     2 : [(3,4),(4,6),(7,1)],
     3 : [(1,9)],
     4 : [(5,11)],
     5 : [(6,14)],
     6 : [(7,5)],
     7 : [(5,8)]
}
INF=1000000
priority_queue=[]
visited=[]
parent=[]
cost=[]
node=7
edge=9

def init():
    for i in range(node+1):
        cost.append(INF)
        parent.append(-1)
        visited.append(0)

def primMST(src):
    bisect.insort(priority_queue,(0,src))       # 0 denotes the distance between source to source
    cost[src]=0

    while len(priority_queue)!=0:
          #pop last item from the list
          pair= priority_queue.pop()
          u=pair[1]
          visited[u]=1
          
          for neighbour in graph[u]:
                v=neighbour[0]
                weight=neighbour[1]
                if(visited[v]==0 and cost[v] > weight):
                    cost[v] = weight
                    bisect.insort(priority_queue,(cost[v],v)) 
                    parent[v]=u
    mst_weight=0
    # Print edges of MST using parent array
    for i in range(src+1,node+1):
        print(str(parent[i])+"->"+str(i)+" = "+str(cost[i]))
        mst_weight+=cost[i]

    print("Minimum weight: "+str(mst_weight))


#driver code
init()
primMST(1)