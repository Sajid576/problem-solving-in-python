'''
Node structure
          1st  |    2nd
          3rd  |    4th
            
'''

adj=[
    (1,2),
    (2,3),
    (3,4),
    (2,6),
    (5,6),
    (6,7),
    (4,7),
    (6,8),
    (6,9),
    (7,10),
    (8,10),
    (9,10),
    (6,11),
    (10,12),
    (11,12)
]
estimated_working_days=[7,12,5,10,5,6,12,10,15,20,10,15]
nodes=[]
visited=[]
queue=[]

def initNodes():
    for i in range(len(estimated_working_days)):
             nodes.append( (i+1,estimated_working_days[i],0,0) )


def perChart(source):
    visited.append(source)
    queue.append(source)

    while queue:
        s = queue.pop(0) 
        #print (s, end = " ") 
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


#print(nodes)
initNodes()
