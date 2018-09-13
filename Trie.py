class TrieNode:

    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.endOfWord = None

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, value):
        current_node = self.root
        for item in value:
            if item not in current_node.children:
                current_node.children[item] = TrieNode(item)
            current_node = current_node.children[item]
        current_node.endOfWord = True

    def numOfWords(self, start):
        words = 0
        node = self.root
        visited, stack = set(), [node]

        prefix = []

        i=0

        while stack:
            curNode = stack.pop()
            #print curNode.value
            if curNode.value != None:
                if start[i] == curNode.value:
                    if i == (len(start) - 1):
                        print "test"
                    i+=1
                    words+=len(curNode.children)

            if curNode.value not in visited:
                visited.add(curNode.value)
                for child in curNode.children:
                    if child not in visited:
                        stack.append(curNode.children[child])
        return prefix

                         
t = Trie()
t.insert("hack")
t.insert("hackerrank")
t.insert("have")
t.insert("pie")
t.insert("work")
print t.numOfWords("ha")
