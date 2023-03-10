
INF=9999
graph=[
    [0,5,INF,10],
    [INF,0,3,INF],
    [INF,INF,0,1],
    [INF,INF,INF,0]
]
node=4
parent=[]

def init():
    for i in range(node):
         parent.append([])
    
    for i in range(node):
        for j in range(node):
             parent[i].append(0)


def floydWarshall():
    for i in range(node):
        for j in range(node):
            if(graph[i][j]==0 or graph[i][j]==INF):
                parent[i][j]=-1
            else:
                parent[i][j]=i
    
    for k in range(node):
        for i in range(node):
            for j in range(node):
                if(graph[i][k] + graph[k][j]<graph[i][j]):
                     graph[i][j]=graph[i][k] + graph[k][j]
                     parent[i][j]=parent[k][j]
    

    for i in range(node):
        if(graph[i][i]):
            print("Negative cycle detected")
            return
    
    print("All pair shortest distances are:  ")
    printShortestDistance()
    print("All pair shortest path are:  ")
    printShortestPath()

def printShortestDistance():
    for i in range(node):
        for j in range(node):
            if(graph[i][j]==INF):
                print("INF",end=' ')
            else:
                print(graph[i][j],end='\t')
        print('\n')

def printShortestPath():
    for i in range(node):
        for j in range(node):
            if(i!=j):
                print("Path from "+str(i)+" to "+str(j)+"  is:  ",end=' ')
                printPath(i,j)
                
            
            
        print('\n')
     
def printPath(i,j):
    path=[]
    #pushing to the front
    path.insert(0,j)
    dest=j
    while(i!=j ):
       
        if(parent[i][j]==-1):
            break
        else:
            j=parent[i][j]
            #pushing to the front
            path.insert(0,j)
            
       
    for i in range(len(path)):
    
        if(len(path)==1 and path[i]==dest):
             print("No path exists ")
        else:
             print(path[i],end=' ')

    print('\n')



#driver code
init()
floydWarshall()