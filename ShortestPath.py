import sys
import heapq

class Edge(object):
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = sys.maxsize

    def __cmp__(self, other_vertex):
        return self.cmp(self.min_distance, other_vertex.min_distance)

    def __lt__(self, other_vertex):
        return self.min_distance < other_vertex.min_distance

class ShortestPath(object):
    def calculate(self, vertex_list, start_vertex):
        q = []
        start_vertex.min_distance = 0
        heapq.heappush(q, start_vertex)
        
        while q:
            min_vertex = heapq.heappop(q)
            for edge in min_vertex.adjacency_list:
                source = edge.start_vertex
                destination = edge.end_vertex
                new_distance = source.min_distance + edge.weight

                if new_distance < destination.min_distance:
                    destination.predecessor = source
                    destination.min_distance = new_distance
                    heapq.heappush(q, destination)


    def get(self, target_vertex):
        print "Shortest path to vertex is {0}".format(target_vertex.min_distance)
        node = target_vertex
        while node:
            print "{0}".format(node.name)
            node = node.predecessor

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')

edge1 = Edge(5, node1, node2)
edge2 = Edge(1, node1, node3)
edge3 = Edge(2, node2, node4)
edge4 = Edge(1, node3, node4)

node1.adjacency_list.append(edge1)
node1.adjacency_list.append(edge2)
node2.adjacency_list.append(edge3)
node3.adjacency_list.append(edge4)

vertex_list = (node1, node2, node3, node4)
a = ShortestPath()
a.calculate(vertex_list, node1)
a.get(node4)

