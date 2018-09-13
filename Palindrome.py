class Dequeue:
	
	def __init__(self):
		self.items = []

	def AddToBegining(self, item):
		self.items.insert(0,item)

	def AddToEnd(self, item):
		self.items.append(item)

	def RemoveFromBegining(self):
		return self.items.pop(0)

	def RemoveFromEnd(self):
		return self.items.pop()
	
	def isEmpty(self):
		return self.items == []

	def Size(self):
		return len(self.items)


def IsPalindrone(word):

	myDequeue = Dequeue()

	for char in word:
		myDequeue.AddToBegining(char)

	palindrone = True

	count = myDequeue.Size()

	while palindrone and count > 1:
		left = myDequeue.RemoveFromBegining()
		right = myDequeue.RemoveFromEnd()
		if left != right:
			palindrone = False
		count -= 2

	if palindrone:
		return True
	else:
		return False

words = ["POOP", "RADAR", "JAMES"]

for word in words:
	print IsPalindrone(word)





