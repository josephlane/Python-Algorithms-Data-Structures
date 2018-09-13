class BinaryCode:

	def decode(self, message):
		Q = [int(message[i]) for i in range(len(message))]
		L = []
		for i in range(0, 2):
			P = [i]
			V = Decrypt(Q, P)
			V = "".join(map(str, V))
			L.append(V)
		return tuple(L)

def Decrypt(Q, P):
	if len(Q) > 0:
		if len(Q) > 1:
			P.append(Q[0] - P[0])
			for i in range(1, len(Q)-1):
				P.append(Q[i] - P[i] - P[i-1])
	encrypted = Encrypt(P)
	if Q != encrypted:
		return "NONE"
	else:
		return P

def Encrypt(P):
	Q = []
	for i in range(0, len(P)):
		if len(P) == 1:
			return P
		else:
			if i == 0:
				Q.append(P[i] + P[i+1])
			elif i == len(P)-1:
				Q.append(P[i-1] + P[i])
			else:
				Q.append(P[i-1] + P[i] + P[i+1])
	return Q

b = BinaryCode()
s = b.decode("123210122")
print s
