# Using a Python list to act as an adjacency list
# ( startingNode,destinationNode,weight)

#graph = [(1, 2, 3), (2, 3, 4), (2, 4, 6), (2, 7, 1), (3, 1, -9),
   #      (4, 5, 11), (5, 6,14), (6, 7, 5), (7, 5, 8)]


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
        for i in range(1,node+1):
            dist[i] = INF
            
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
        for j in range(edge):
            u = graph[j][0]
            v = graph[j][1]
            w = graph[j][2]
            if (visited[u] == 0 and (dist[v] > dist[u] + w)):
                dist[v] = dist[u] + w
                print(str(u) + "->" + str(v))
                negative_cycle_node.append(u)
                visited[u] = 1
            
        print(negative_cycle_node)

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