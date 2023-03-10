from collections import defaultdict


# Using a Python dictionary to act as an adjacency list
graph = {
    1: [2],
    2: [3, 4],
    3: [1],
    4: [5],
    5: [6],
    6: [7],
    7: [5]
}


def generate_transpose(graph):
    transpose = {}
    for key in graph:
        transpose[key] = []

    for key in graph:
        for node in graph[key]:
            transpose[node].append(key)

    return transpose


transpose_graph = generate_transpose(graph)
print(transpose_graph)
# transpose_graph = {
#     1: [3],
#     2: [1],
#     3: [2],
#     4: [2],
#     5: [4, 7],
#     6: [5],
#     7: [6]
# }

visited = {}  # dictionary to keep track of visited nodes.
result = []   # result stack to push the result
WHITE = 1
GREY = 2
BLACK = 3
components = defaultdict(list)


def dfs(visited, graph, node):
    visited[node] = GREY
    for neighbour in graph[node]:
        if visited[neighbour] == WHITE:
            dfs(visited, graph, neighbour)

    visited[node] = BLACK
    # pushing to the result stack
    result.append(node)


def next_dfs(visited, graph, node, mark):

    components[mark].append(node)
    visited[node] = GREY
    for neighbour in graph[node]:
        if visited[neighbour] == WHITE:
            next_dfs(visited, graph, neighbour, mark)


print()
print()
# Driver Code
for i in range(1, 8):
    visited[i] = WHITE

print(visited)
for i in range(1, 8):
    if(visited[i] == WHITE):
        dfs(visited, graph, i)


mark = 0
for i in range(1, 8):
    visited[i] = WHITE


while len(result) != 0:
    u = result.pop()
    if(visited[u] == WHITE):
        mark = mark+1
        next_dfs(visited, transpose_graph, u, mark)

numberOfcycles = 0

print("Number of components:  "+str(mark))
for key, value in components.items():
    Size = len(components[key])
    if(Size >= 2):
        numberOfcycles += 1
    print(components[key])

print("Number of cycle is:  "+str(numberOfcycles))
