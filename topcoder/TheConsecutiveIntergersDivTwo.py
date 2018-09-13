class TheConsecutiveIntergersDivTwo:
	def find(self, numbers, k):
		numbers = list(numbers)
		numbers.sort(reverse=True)
		final = []
		if k > 1:
			print numbers
			for i in range(k, -1, -1):
				diff = abs(numbers[i] - (numbers[i-1] - 1))
				final.append(diff)
		else:
			return 0

		return final

b = TheConsecutiveIntergersDivTwo()

print b.find((-96, -53, 82, -24, 6, -75), 2)

