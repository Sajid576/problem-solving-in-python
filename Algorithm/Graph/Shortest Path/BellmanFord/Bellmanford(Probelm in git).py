'''
1) Finding the number of negative cycle
2) Find which negative cycle node is included in which negative cycle?
'''
# ( startingNode,destinationNode,weight)
from collections import defaultdict
graph=[(1,2,1),(2,1,-2),(2,5,8),(5,3,7),(5,4,-8),(4,6,10),(6,5,2),(4,7,8),
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
            u = graph[j][0]
            v = graph[j][1]
            w = graph[j][2]
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
            u = graph[j][0]
            v = graph[j][1]
            w = graph[j][2]
            if (dist[v] > dist[u] + w):
                dist[v] = dist[u] + w
                parent[v] = u
        print("negative cycle found")
        print(graph)
        negative_cycle_node = []
        #dist = [INF] * n
        noOfcycle = 0
        noOfcomponent =1 
        component=defaultdict(list) #track with which nodes they are making cycle simalar as scc
        for j in range(edge):
            u = graph[j][0]
            v = graph[j][1]
            w = graph[j][2]
            if (visited[u] == 0 and (dist[v] > dist[u] + w)):
                dist[v] = dist[u] + w
                print(str(u) + "->" + str(v))
                component[noOfcomponent].append(u)
                negative_cycle_node.append(u)
                visited[u] = 1
                if v in negative_cycle_node:
                    noOfcycle=noOfcycle+1
                    noOfcomponent=noOfcomponent+1
        print(negative_cycle_node)
        print('Number of negative cylce: ',noOfcycle)
        print(component)
        
        node_query=int(input())

        for x,y in component.items():
            if node_query in y:
                print('this node is a cycle with',component[x])
            
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
init(node)
bellManFord(1)
