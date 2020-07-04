'''
taking input from user
first line query
second line node and edge
third line is for path(strting vertex and ending vertex)
forth line for starting node from which the dfs will run

'''
from collections import defaultdict 
print("how many query you want?")
query = int(input())
def bfs(visited, graph, node):
    distance = 0
    height=0
    visited.append(node)
    queue.append(node)
    minimum.pop(int(node))
    while queue:
        distance=height
        s = queue.pop(0) 
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                height=distance+6
                minimum[int(neighbour)]=height
                #dis.append(height)
    sorted_items=sorted(minimum.items())
    for x,y in sorted_items:
        dis.append(int(y))
    
               
    print(" ".join(map(str,dis)))



for q in range(query):
    node, edge = input().split() 
    node = int(node)
    edge = int(edge)
    graph = defaultdict(list) 
    i = 0 
    while i<edge:
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
        i+=1
    start =input()
    
    dis = [] # in that i will push the dis of dest from src
    minimum={}       # this dic needed for sorting acording to the key
    for j in range(1,node+1):
        minimum[j]=-1
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue
    bfs(visited, graph, start)
