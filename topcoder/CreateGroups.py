class CreateGroups:
	def minChanges(self, groups, minSize, maxSize):
		less = 0
		more = 0
		total = sum(groups)
		size = len(groups)

		if (total > (maxSize * size)) or (total < (minSize * size)):
			return -1
		for group in groups:
			if group > maxSize:
				more += (group - maxSize)
			elif group < minSize:
				less += (minSize - group)

		return max(less, more)


s = CreateGroups()

print s.minChanges((1, 10, 10), 9, 20)