import unittest

class Node:

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def setNext(self, next):
		self.next = next

	def getNext(self):
		return self.next

class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	def add(self, value):
		node = Node(value)
		node.setNext(self.head)
		self.head = node
		self.size += 1

	def remove(self, value):
		current = self.head
		previous = None
		found = False

		while not found:
			if current.data == value:
				found = True
				self.size-=1
			else:
				previous = current
				current = current.next

		if previous == None: # Head node
			self.head = current.next
		else: # None head node
			previous.setNext(current.next)

		return found

	def search(self, value):
		current = self.head
		found = False

		while current and not found:
			if current.getData() == value:
				found = True
			else:
				current = current.next

		return found

	def size(self):
		return self.size

class TestSinglyLinkedList(unittest.TestCase):
	"""
	Test Singly Linked List Implementation
	"""

	def test_singly_linked_list(self):
		self.sl = singly_linked_list.SinglyLinkedList()
		self.sl.add(10)
		self.sl.add(5)
		self.sl.add(30)
		self.sl.remove(30)

		self.assertEqual(self.sl.size, 2)
		self.assertEqual(self.sl.search(30), False)
		self.assertEqual(self.sl.search(5),True)
		self.assertEqual(self.sl.search(10), True)
		self.assertEqual(self.sl.remove(5), True)
		self.assertEqual(self.sl.remove(10), True)
		self.assertEqual(self.sl.size, 0)







