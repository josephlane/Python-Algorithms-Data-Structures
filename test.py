import unittest
from random import randint

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):

	def __init__(self):
		self.node = None

	def insert(self, value):
		if not self.node: #if there is no root, add one
			#print "new node: " + str(value)
			self.node = Node(value)
		else: #else loop through nodes to find insert spot
			curNode = self.node
			while curNode != None: #current node is not empty
				#print "new loop"
				if value < curNode.value:
					#print "value is less than current node"					
					#print curNode.value, value
					if curNode.left == None: #if at end of node, insert
						#print "currently, there is no left node"
						curNode.left = Node(value)
						break
					else:
						#print "left node found"
						curNode = curNode.left
				else:
					if curNode.right == None:
						#print "currently, thre is no right node"
						curNode.right = Node(value)
						break
					else:
						#print "right node found"
						curNode = curNode.right

	def find(self, value):
		if not self.node:
			return False
		else:
			curNode = self.node
			while curNode:
				if curNode.value == value:
					return True
				elif value < curNode.value:
					curNode = curNode.left
				else:
					curNode = curNode.right	
			return False	


def inOrderTraversal(node):
	if node != None:
		inOrderTraversal(node.left)
		print node.value
		inOrderTraversal(node.right)

def preOrderTraversal(node):
	if node != None:
		print node.value
		preOrderTraversal(node.left)
		preOrderTraversal(node.right)

def postOrderTraversal(node):
	if node != None:
		preOrderTraversal(node.left)
		preOrderTraversal(node.right)
		print node.value

b = [randint(1,100000) for i in range(1,10)]
print b

a = BinaryTree()

for s in b:
	a.insert(s)

# print a.node.value
# print a.node.left.value
# print a.node.right.value

inOrderTraversal(a.node)

print a.find(1)








