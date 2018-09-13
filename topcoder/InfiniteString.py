
#approach - sets allow you to contain on unique values. So we can get the unique values for both data sources and compare them
class InfiniteString:
	def equal(self, s, t):
		return "Equal" if s * len(t) == t * len(s) else "Not equal"

b = InfiniteString()
print b.equal("aaaaa", "aaaaaa")

a = "abc"

b = "abcabc"

print a * len(b)
print b * len(a)