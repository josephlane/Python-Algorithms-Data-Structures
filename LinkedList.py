#LinkedList examples

class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, data):
		self.data = data

	def setNext(self, next):
		self.next = next

class UnorderedList:

	def __init__(self):
		self.head = None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def isEmpty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found and current:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
                if found:
		    if previous == None:
	                self.head = current.getNext()
		    else:
			previous.setNext(current.getNext())

if __name__  == "main":

    plist = UnorderedList()
    plist.add(55)
    plist.add(56)
    plist.add(57)
    plist.add(58)
    plist.remove(57)

    print plist.search(57)
