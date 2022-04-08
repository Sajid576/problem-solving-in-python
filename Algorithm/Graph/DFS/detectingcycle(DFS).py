from collections import defaultdict
WHITE = 1
GREY = 2
BLACK = 3

stack = []

# initializing a default dictionary with list
graph = defaultdict(list)

# dictionary to keep track of visited nodes.
visited = defaultdict(lambda: WHITE)
flag = False


def dfs(visited, graph, node):
    stack.append(node)
    print(node)
    visited[node] = GREY
    for neighbour in graph[node]:
        if neighbour in stack:  # alredy present in the stack that means it is already visited
            global flag
            flag = True
            break

        if visited[neighbour] == WHITE:
            dfs(visited, graph, neighbour)
    visited[node] = BLACK


# Driver Code
node, edge = input().split()
starting_node = input()

for i in range(int(edge)):
    a, b = input().split()
    graph[a].append(b)


dfs(visited, graph, starting_node)
if flag == True:
    print('this graph has a cycle')
else:
    print('this graph has no cycle')
