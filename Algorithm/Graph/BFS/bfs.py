# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
from collections import defaultdict


visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
#initializing a default dictionary with list
graph=defaultdict(list) 

parent=[]
dist=[]

def init(n):
  for i in range(n+1):
      dist.append(-1)
  for i in range(n+1):
      parent.append(-1)

def shortestPath(i):
    if(parent[i]==-1):
          print(i,end=' ')
          return 
     
    shortestPath(parent[i])
    print(i,end=' ')

def ShortestDistance(source):
    for i in range(1,len(visited)+2):
        if(i != source):
            if(dist[i]!=-1):
                dist[i]*=6
            print("\n"+str(i)+"->"+str(dist[i]),end='\n')
            print("Shortest path: ")
            shortestPath(i)
              
def bfs(visited, graph, source):
  visited.append(source)
  queue.append(source)
  dist[source]=0

  print("BFS traversals: ")
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        dist[neighbour]=dist[s]+1
        parent[neighbour]=s

  print("\n")
  ShortestDistance(source)

# Driver Code

node,edge=input().split()



for i in range(int(edge)):
    a,b= input().split()
    graph[int(a)].append(int(b))
    graph[int(b)].append(int(a))

starting_node=int(input())

init(int(node))
bfs(visited, graph, starting_node)