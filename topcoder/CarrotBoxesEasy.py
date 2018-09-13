class CarrotBoxesEasy:
	def theIndex(self, carrots, K):
		carrots = list(carrots)
		index = 0
		while K > 0:
			index = carrots.index(max(carrots))
			carrots[index] -= 1
			K -= 1
		return index
		