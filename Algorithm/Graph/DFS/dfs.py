#https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python#:~:text=Depth-first%20search%20(DFS),structures%20like%20dictionaries%20and%20sets.

# Using a Python dictionary to act as an adjacency list
from collections import defaultdict
WHITE=1
GREY=2
BLACK=3



#initializing a default dictionary with list
graph=defaultdict(list) 

 # dictionary to keep track of visited nodes.
visited =defaultdict(lambda: WHITE)




def dfs(visited, graph, node):
    
    print (node)
    visited[node]=GREY    
    for neighbour in graph[node]:
        if visited[neighbour]==WHITE:
            dfs(visited, graph, neighbour)
     
    visited[node]=BLACK


node,edge=input().split()
starting_node=input()

for i in range(int(edge)):
    a,b= input().split()
    graph[a].append(b)
# Driver Code
dfs(visited, graph, starting_node)