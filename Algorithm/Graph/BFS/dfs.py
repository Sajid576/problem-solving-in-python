#https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python#:~:text=Depth-first%20search%20(DFS),structures%20like%20dictionaries%20and%20sets.

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited ={} # dictionary to keep track of visited nodes.
WHITE=1
GREY=2
BLACK=3

def dfs(visited, graph, node):
    
    print (node)
    visited[node]=GREY    
    for neighbour in graph[node]:
        if visited[neighbour]==WHITE:
            dfs(visited, graph, neighbour)
     
    visited[node]=BLACK

# Driver Code

visited['A']=WHITE
visited['B']=WHITE
visited['C']=WHITE
visited['D']=WHITE
visited['E']=WHITE
visited['F']=WHITE


print(visited)
dfs(visited, graph, 'A')