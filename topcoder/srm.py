class Hexspeak:
	def decode(self, ciphertext):
		x = ['2','3','4','5','6','7','8','9']
		a = hex(ciphertext)
		a = a[2:]
		a = list(a)
		p = False
		for i in range(0, len(a)):
			if a[i] == '1':
				a[i] = 'I'
			elif a[i] == '0':
				a[i] = 'O'
			elif a[i] in x:
				p = True	 

		a = "".join(map(str, a) )
		a = a.upper()	

		if p:
			return "Error!"
		else:
			return a

	def decode2(self, ciphertext):
		T = "OI........ABCDEFG"
		ret = ""
		while ciphertext > 0:
			c, ciphertext = ciphertext % 16, ciphertext / 16
			if T[c] == ".":
				return "Error!"
			ret = T[c]+ret
		return ret

a = 3405691582
s = Hexspeak()
print s.decode2(a)
print s.decode(a)

