class DivisorDigits:
	def howMany(self, number):
		x = list(number)
		count = 0
		for a in x:
			if a > 0:
				if number % a == 0:
					count += 1
		return count

d = DivisorDigits()
print d.howMany(12345)

