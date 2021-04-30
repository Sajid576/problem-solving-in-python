

class Edge:
    def __init__(self, u, v,w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return str(self.u)+","+str(self.v)+","+str(self.w)

parent=[]
edges=[]

def make_set(x):
    parent[x] = x

# find the representative of the set of a particular element
def find_parent(r):
    if(parent[r] == r):
        return r
 
    else:
        parent[r] = find_parent(parent[r])
        
    
def mst(n):
    # sorting the edges by weight
    edges.sort(key=lambda x: x.w)
    
    for i in range(n+1):
        make_set(i)
    
    Count = 0
    min_cost = 0
    for i in range(len(edges)):
        u = find_parent(edges[i].u)
        v = find_parent(edges[i].v)
        print('')
        print('u(boss):'+str(u)+" u:"+str(edges[i].u))
        print('v:'+str(v))
        print('i:'+str(i))
        for i in range(1,n+1):
            print(str(parent[i]) ,end=' ')
        if (u != v) :
           
            parent[u] = v
            Count+=1;
            min_cost += edges[i].w
            if (Count == n - 1):
                break

    return min_cost   


def display(min_cost,n):
    print("Minimum cost is: ",str(min_cost))
    for i in range(n):
        print(str(i)+"--"+str(parent[i]))

def initiate_parent(n):
    for i in range(n+1):
        parent.append(-1)

def add_Edge(u,v,w):
    edges.append(Edge(u,v,w))


file = open("input.txt","r")
x=file.readline().split(' ')
nodes_num=int(x[0])
edges_num=int(x[1])

initiate_parent(10001)

for i in range(edges_num):
    x=file.readline().split(' ')
    u=int(x[0])
    v=int(x[1])
    w=int(x[2])
    add_Edge(u,v,w)

'''
for i in range(len(edges)):
    print(edges[i])
'''  

min_cost=mst(nodes_num)
display(min_cost,nodes_num)


