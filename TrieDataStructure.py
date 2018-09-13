class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isWord = False
        self.size = 0

class Trie:
    def __init__(self):
        self.root = TrieNode("*") #represents root node

    def add(self, word):
        curNode = self.root
        for char in word:
            #print char
            if char not in curNode.children:
                curNode.children[char] = TrieNode(char) #add it
            curNode = curNode.children[char] #move to next char/node
            curNode.size += 1
            #print "The current Node is {0} with a count of {1} children".format(curNode.char, curNode.size)
           
        curNode.isWord = True

    def isValidWord(self, word):
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                return False
            else:
                curNode = curNode.children[char]
        return curNode.isWord        

    def walkNodes(self, node, word):
        curNode = node
        curWord = word
        print curNode.children
        curWord += curNode.char
        #print curWord

        if curNode.children:
            for value in curNode.children.itervalues():
                print value.char
                return self.walkNodes(value, curWord)
        else:
            return curWord

a = Trie()

a.add("app")
a.add("at")
a.add("all")
a.add("boot")
a.add("boat")
# a.add("approach")
# a.add("attitude")
# a.add("alteration")
# a.add("battle")
# a.add("break")
# a.add("breast")
# a.add("cook")

#print a.root.children["a"].size
#print a.root.children["b"].size
# print a.root.children["c"].size
#print a.isValidWord("zz")node.char
words = []

for value in a.root.children.itervalues():
    words.append(a.walkNodes(value, ""))
print words








