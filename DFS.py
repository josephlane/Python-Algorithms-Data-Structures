class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False

class Graph(object):
    def dfs(self, node):
        node.visited = True
        print "{0}".format(node.name)

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)



node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')
node8 = Node('H')

node1.adjacencyList.append(node2)
node2.adjacencyList.append(node3)
node3.adjacencyList.append(node4)
node4.adjacencyList.append(node5)
node5.adjacencyList.append(node6)
node6.adjacencyList.append(node7)

g = Graph()

g.dfs(node1)
