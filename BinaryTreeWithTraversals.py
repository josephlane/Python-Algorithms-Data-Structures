class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def preorder(tree):
    if tree:
        print tree.getRootVal()
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

r = BinaryTree("CAB")
r.insertLeft("FAC")
r.insertRight("BCN")

z = r.getRightChild()
z.insertLeft("RAC")
z.insertRight("PRD")


b = r.getLeftChild()
b.insertLeft("PAR")

c = b.getLeftChild()
c.insertRight("MCN")

d = c.getRightChild()
d.insertLeft("PDW")
d.insertRight("ZRN")

preorder(r)
print "----"
inorder(r)
print "----"
postorder(r)








