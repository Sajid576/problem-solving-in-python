

# Using a Python dictionary to act as an adjacency list
graph = {
     0 : [1,3],
     1 : [2],
     2 : [3,4],
     3 : [4],
     4 : [],
     5 : [1],
}

visited ={} # dictionary to keep track of visited nodes.
result=[]   #result stack to push the result
WHITE=1
GREY=2
BLACK=3

def dfs(visited, graph, node):
    
    
    visited[node]=GREY    
    for neighbour in graph[node]:
        if visited[neighbour]==WHITE:
            dfs(visited, graph, neighbour)
     
    visited[node]=BLACK
    result.append(node)

# Driver Code
for i in range(6):
    visited[i]=WHITE

#print(visited)
for i in range(0,6):
    if(visited[i]==WHITE):
        dfs(visited, graph, i)
print(result)