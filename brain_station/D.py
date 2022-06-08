from collections import defaultdict
import bisect

# Using a Python dictionary to act as an adjacency list
# startingNode--> (destinationNode,weight)
# 1: [(2, 24), (4, 20), (3, 3)],
# 2: [(1, 24)],
# 3: [(1, 3), (4, 12)],
# 4: [(3, 12), (1, 20)]
graph = defaultdict(list)

INF = 1000000
priority_queue = []
visited = []
dist = []
parent = []
# node = 4
# edge = 4


def init(n):
    for i in range(n+1):
        visited.append(0)

    for i in range(n+1):
        dist.append(INF)

    for i in range(n+1):
        parent.append(-1)


def dijkstra(source):

    # 0 denotes the cost of source node
    bisect.insort(priority_queue, (0, source))
    dist[source] = 0

    while len(priority_queue) != 0:
        # pop first item from the list
        pair = priority_queue.pop(0)
        u = pair[1]
        visited[u] = 1
        # print(pair)
        for neighbour in graph[u]:
            v = neighbour[0]
            weight = neighbour[1]

            # print(str((u, v))+"-- "+str(dist[u]) +
            #       "+"+str(weight)+"<"+str(dist[v]))
            if(visited[v] == 0 and dist[v] > dist[u]+weight):
                dist[v] = dist[u]+weight
                bisect.insort(priority_queue, (dist[v], v))
                parent[v] = u

    costCalculation()


def shortestPath(i):
    if(parent[i] == -1):
        print(i, end=' ')
        return

    shortestPath(parent[i])
    print(i, end=' ')


def costCalculation():
    destinationNode = int(node)
    shortestPath(destinationNode)


# driver code
node, edge = input().split()
init(int(node))
for i in range(int(edge)):
    a, b, c = input().split()

    graph[int(a)].append((int(b), int(c)))
    graph[int(b)].append((int(a), int(c)))


dijkstra(1)
