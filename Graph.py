graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):

    visited = set()

    stack = [start]

    while stack:
        vertex = stack.pop()
        print "Current Vertex: " + vertex
        if vertex not in visited:
            visited.add(vertex)
            #only add child nodes that have not been visisted
            print graph[vertex], visited
            stack.extend(graph[vertex] - visited)

    return visited

print dfs(graph, 'A')

