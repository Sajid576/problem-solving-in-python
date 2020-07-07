from collections import defaultdict
import numpy as np
components=defaultdict(list)
def SCC():
    graph = {
     1 : [2],
     2 : [1,5],
     5 : [3,4],
     3 : [],
     4 : [6,7],
     
     6 : [5],
     7 : [8],
     8 : [9],
     9 : [7]
    }
    transpose_graph = {
        1 : [2],
        2 : [1],
        3 : [5],
        4 : [5],
        5 : [2,6],
        6 : [4],
        7 : [4,9],
        8 : [7],
        9 : [8],
    } 

    visited ={} # dictionary to keep track of visited nodes.
    result=[]   # result stack to push the result
    WHITE=1
    GREY=2
    BLACK=3
    

    def dfs(visited, graph, node): 
        visited[node]=GREY    
        for neighbour in graph[node]:
            if visited[neighbour]==WHITE:
                dfs(visited, graph, neighbour)
    
        visited[node]=BLACK
        #pushing to the result stack 
        result.append(node)


    def next_dfs(visited, graph, node,mark):
        
        components[mark].append(node)
        visited[node]=GREY    
        for neighbour in graph[node]:
            if visited[neighbour]==WHITE:
                next_dfs(visited, graph, neighbour,mark)
         
# Driver Code
    for i in range(1,10):
        visited[i]=WHITE
    
    print(visited)
    for i in range(1,10):
        if(visited[i]==WHITE):
            dfs(visited, graph, i)
    
    
    mark=0
    for i in range(1,10):
        visited[i]=WHITE


    while len(result)!=0:
        u=result.pop()
        if( visited[u]==WHITE):
            mark=mark+1
            next_dfs(visited,transpose_graph,u,mark)
    
    numberOfcycles=0
    print("Number of components:  "+str(mark))
    for key, value in components.items():
        Size=len(components[key])
        if(Size>=2):
            numberOfcycles+=1
        print(components[key])
        
    print("Number of cycle is:  "+str(numberOfcycles))


graph1=[(1,2,1),(2,1,-2),(2,5,8),(5,3,7),(5,4,-8),(4,6,10),(6,5,2),(4,7,8),
        (7,8,-2),(8,9,1),(9,7,-3)  ]

INF = 1000000
visited = []
dist = []
parent = []
node = 9
edge = 11


def init(n):
    for i in range(n + 1):
        visited.append(0)

    for i in range(n + 1):
        dist.append(INF)

    for i in range(n + 1):
        parent.append(-1)

def bellManFord(source):
    dist[source] = 0
    ck = True
    # in (node-1) range it will be rested 
    for i in range(node):
        ck = True
        for j in range(edge):
            u = graph1[j][0]
            v = graph1[j][1]
            w = graph1[j][2]
            if (dist[v] > dist[u] + w):
                dist[v] = dist[u] + w
                parent[v] = u
                ck = False
    if ck:
        print("No negative cycle found")
        #costCalculation(source)
    else:
        for i in range(8):
            dist[i] = 10000
        for j in range(edge):
            u = graph1[j][0]
            v = graph1[j][1]
            w = graph1[j][2]
            if (dist[v] > dist[u] + w):
                dist[v] = dist[u] + w
                parent[v] = u
        print("negative cycle found")
        print(graph1)
        negative_cycle_node = []
        #dist = [INF] * n
        
        for j in range(edge):
            u = graph1[j][0]
            v = graph1[j][1]
            w = graph1[j][2]
            if (visited[u] == 0 and (dist[v] > dist[u] + w)):
                dist[v] = dist[u] + w
                print(str(u) + "->" + str(v))
                negative_cycle_node.append(u)
                visited[u] = 1
                
        print(negative_cycle_node)
        
         
        noOfnegativecycle = 0
        print('Number of negative cycle are :')
        for x,y in components.items():
            if y[0] in negative_cycle_node:
                noOfnegativecycle=noOfnegativecycle+1
                print(components[x])
             
        print('no of negative cycle',noOfnegativecycle)   
        node_query=int(input('enter a node to see which cycle it belongs '))
        
        for x,y in components.items():
            if node_query in y:
                print('this node is a cycle with',components[x])
            
def shortestPath(i):
    if (parent[i] == -1):
        print(i, end=' ')
        return

    shortestPath(parent[i])
    print(i, end=' ')

def costCalculation(source):
    # print(len(dist))
    print("Source -----Destination------Distance")
    for i in range(source, len(dist)):
        print(str(source) + "------------->" + str(i) + "-----" + str(dist[i]))
        print("Shortest path: ", end=' ')
        shortestPath(i)
        print('\n')


# driver code
SCC()
init(node)
bellManFord(1)