"""

Implementation of Breadth First Search

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False

class BreadthFirstSearch(object):
    def bfs(self, node):
        nodes = [node]
        while nodes:
            sub = nodes.pop(0)
            if not sub.visited:
                print sub.value
                sub.visited = True
                for child in sub.children:
                    nodes.append(child)
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.children = [b, c]
c.children = [d]
b = BreadthFirstSearch()
b.bfs(a)

