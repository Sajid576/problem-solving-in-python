# Using a Python list to act as an adjacency list
# ( startingNode,destinationNode,weight)

graph=[(1,2,3),(2,3,4),(2,4,6),(2,7,1),(3,1,-9),
        (4,5,11),(5,6,14),(6,7,5),(7,5,8)]

INF=1000000
visited=[]
dist=[]
parent=[]
node=7
edge=9

def init(n):
     for i in range(n+1):
          visited.append(0)

     for i in range(n+1):
          dist.append(INF)

     for i in range(n+1):
          parent.append(-1)
     

def bellManFord(source):
    dist[source]=0
    
    ck=1
    for i in range(1,node*node):      
         
            ck=1
            for j in range(edge):
                 u=graph[j][0]
                 v=graph[j][1]
                 w=graph[j][2]
                 #print(str((u,v))+str(dist[v])+"=="+str(dist[u])+"+"+str(w))

                 if( dist[v]>dist[u]+w):
                        dist[v]=dist[u]+w
                        parent[v]=u
                        ck=0

    if(ck==1):
        print("No negative cycle found")
        costCalculation(source)
    else:
        
        print("negative cycle found")
        negative_cycle_node=[]
        for j in range(edge):
                 u=graph[j][0]
                 v=graph[j][1]
                 w=graph[j][2]

                 print(str((u,v))+str(dist[v])+"=="+str(dist[u])+"+"+str(w))

                 if(visited[u]==0 and (dist[v]>dist[u]+w)):
                        dist[v]=dist[u]+w
                        visited[u]=1
                        print(str(u)+"->"+str(v))
                        negative_cycle_node.append(u)
        
        print_negative_cycle_node(negative_cycle_node)


def print_negative_cycle_node(negative_cycle_node):
    print(negative_cycle_node)

def shortestPath(i):
     if(parent[i]==-1):
          print(i,end=' ')
          return 
     
     shortestPath(parent[i])
     print(i,end=' ')

def costCalculation(source):
     #print(len(dist))
     print("Source -----Destination------Distance")
     for i in range(source,len(dist)):
          print(str(source)+"------------->"+str(i)+"-----"+str(dist[i]))
          print("Shortest path: ",end=' ')
          shortestPath(i)
          print('\n')


#driver code
init(node)
bellManFord(1)



