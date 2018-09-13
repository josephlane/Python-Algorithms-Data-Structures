#IdentifyWood

class IdentifyWood:
	def check(self, s, t):
		
		s = [s[i] for i in range(0, len(s))]
		t = [t[i] for i in range(0, len(t))]	

		found = (s == t)
		iteration = 1
		lastCharOfT = t
		lastCharOfS = s

		#if len > 1, set last char
		if len(s) > 1 and len(t) > 1:
			lastCharOfT = t[len(t) - 1]
			lastCharOfS = s[len(s) - 1]


		while not found and len(s) > 2 and len(t) > 2:

			if lastCharOfS != lastCharOfT:

				s.pop(s.index(lastCharOfS))
			else:
				if iteration != len(t):
					iteration += 1
					lastCharOfT = t[len(t) - iteration]

			lastCharOfS = s[len(s) - iteration]
			print 'test'
			if s == t:
			    found = True

		if found:
			return "Yep, it's wood."
		else:
			return "Nope."

	def check2(self, s, t):
		m = 0
		for x in s:
			if x == t[m]:
				m+=1
				if m == len(t):
					return "Yep, it's wood."
		return "Nope."

s = IdentifyWood()

print s.check("oxoxoxox", "xxx")

