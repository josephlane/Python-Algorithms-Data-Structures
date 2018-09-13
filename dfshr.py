def bfs(g, startingNode):
    visited, queue = set(), [startingNode, None]
    distances = {}
    distance = 0
    while queue:
        
        node = queue.pop(0)
        
        if node != None:
            if node not in visited:
                #print "Current Node: " + str(node)
                #print "Current level: " + str(distance)
                #print "Node Children: "
                #print g[node]
                #print "Current Queue: "
                #print queue
                #print "----------------"
                #print "----------------"
                
                visited.add(node)

                if node != startingNode and g[node] != set():
                    distances[int(node)] = distance

                addLevel = False
                
                for child in g[str(node)]:
                    if child not in visited:
                        queue.append(child)
                        addLevel = True

                if addLevel:
                    queue.append(None)

        else:
            distance += 6

    for node in g:
        if node not in visited:
            distances[int(node)] = -1
     
    return distances
 
def buildGraph(numOfNodes, edges):
    
    g = {}

    
    for i in range(1, numOfNodes + 1):
        g[str(i)] = set()
        
    for edge in edges:
        if str(edge[0]) in g:
            g[str(edge[0])].add(edge[1])
            g[str(edge[1])].add(edge[0])
        else:
            g[str(edge[0])] = set(edge[1])
            g[str(edge[1])] = set(edge[0]) 
    return g
    
#first param
numOfQueries = raw_input().strip()
numOfQueries = int(numOfQueries)

sd = []

for x in range(numOfQueries):


    #second param, #third param
    numOfNodes, numOfEdges = raw_input().strip().split(' ')
    numOfNodes, numOfEdges = int(numOfNodes), int(numOfEdges)

    edges = []


    for i in range(numOfEdges):
 #       iteration of params
        n,e = raw_input().strip().split(' ')
        edges.append([n,e])


        #last param
    startingNode = raw_input().strip()

    g = buildGraph(numOfNodes, edges)

    shortestDistances = bfs(g, startingNode)

    sd.append(' '.join(str(shortestDistances[path]) for path in sorted(shortestDistances.keys())))

for i in sd:
    print i
