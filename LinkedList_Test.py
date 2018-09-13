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

class UnOrderedList:

	def __init__(self):
		self.head = None
		self.next = None

	def add(self, data):
		data = Node(data)
		data.setNext(self.head)
		self.head = data

	def isEmpty(self):
		return self.head == None

	def size(self):
		count = 0
		current = self.head

		while current != None
			current = current.getNext()
			count += 1

		return count

	def search(self, data):
		found = False
		current = self.head	

		while not found and current != None:
			if current.getData() == data:
				found = True
			else:
				current = current.getNext()
		return found

	def delete(self, data):
		found = False
		current = self.head
		previous = None

		while not found and current != None:
			if current.getData() == data:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getData()
		else:
			previous.setNext(current.getNext())






