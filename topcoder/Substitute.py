class Substitute:
	def getValue(self, key, code):
		count = ""
		for i in xrange(0, len(code)):
			if code[i] in key:
				pos = key.index(code[i])
				if (pos + 1) == len(key):
					count += str(0)
				else:
					count += str(pos + 1)

		return int(count)

	def getValue2(self, key, code):
		res = ""
		for c in code:
			if c in key:
				res += str((key.index(c) + 1) % 10)
		return int(res)


key1 = "TRADINGFEW"
code1 = "LGXWEV"

key2 = "CRYSTALBUM"
code2 = "MMA"

key3 = "ABCDEFGHIJ"
code3 = "XJ"

b = Substitute()

print b.getValue(key1, code1)
print b.getValue(key2, code2)
print b.getValue(key3, code3)

print b.getValue2(key1, code1)
print b.getValue2(key2, code2)
print b.getValue2(key3, code3)
