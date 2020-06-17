# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
from collections import defaultdict

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
#initializing a default dictionary with list
graph=defaultdict(list) 

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code

node,edge=input().split()
starting_node=input()


for i in range(int(edge)):
    a,b= input().split()
    graph[a].append(b)
    

bfs(visited, graph, starting_node)