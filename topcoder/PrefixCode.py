class PrefixCode:
	def isOne(self, words):
		print words
		code = False
		result = ""
		index = ""
		for i in range(0, len(words)):
			print "-" + str(words[i])
			for p in range(0, len(words)):

				if words[i] != words[p]:
					print "--" + str(words[p])					
					if words[p] in words[i]:
						index = p
					elif words[p] in words[i]:
						index = i
					code = True
						

		if code:
			return "No, {0}".format(index)
		else:
			return "Yes"

s = {"no", "nosy", "neighbors", "needed"}

x = {"10001", "011", "100", "001", "10"}

b = PrefixCode()
p = enumerate(s)
p = list(p)
print b.isOne(p)