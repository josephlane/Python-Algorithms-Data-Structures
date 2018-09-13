class CheatingQuiz:
	def howMany(self, answers):
		result = []
		answers = list(answers)
		for i in xrange(len(answers)):
			a = set(answers[i:])
			result.append(len(a))
		return tuple(result)

	def howManyCompact(self, answers):
		return tuple([len(set(answers[i:])) for i in xrange(len(answers))])


c = "CAAAAAC"
c = "BBCA"
c = "BACACABCBBBBCAAAAACCCABBCAA"
b = CheatingQuiz()
print b.howMany(c)
print b.howManyCompact(c)