class YahtzeeScore:
	def maxPoints(self, toss):
		toss = list(toss)
		toss.sort()
		maxVal = max(toss)
		k = len(toss) - 1
		while k > 0:	
			if toss[k] == toss[k-1] and (toss[k] + toss[k-1]) > maxVal:
				maxVal = toss[k] + toss[k-1]
				break
			k -= 1
		return maxVal

b = YahtzeeScore()
print b.maxPoints(( 5, 3, 5, 3, 3 ))
