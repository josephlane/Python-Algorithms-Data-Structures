class ContestCoordinator:
	def bestAverage(self, scores):
		scores = sorted(scores)
		min = 0
		max = 0
		total = 0
		size = len(scores)
		if size > 2:
			min = scores[0]
			max = scores[size -1]
			if min != max:
				avgSize = 0
				for score in scores:
					if (score != min) and (score != max):
						total += score
						avgSize += 1
				return float(total) / float(avgSize)
			else:
				return float(scores[0])
		else:
			return float(scores[0])

b = ContestCoordinator()
print b.bestAverage((1,13,8,6,7,9))