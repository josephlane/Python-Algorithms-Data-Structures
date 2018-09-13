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
		a = a.replace("L", "")	

		if p:
			return "Error!"
		else:
			return a

a = 3405691582
s = Hexspeak()
print s.decode2(a)
print s.decode(a)

