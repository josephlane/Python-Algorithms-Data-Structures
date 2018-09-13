class TaroJiroDividing:
	def getNumber(self, A, B):
		R1, R2, C = [A], [B], 0
		while A % 2 == 0:
			R1.append(A / 2)
			A = A / 2			
		while B % 2 == 0:
			R2.append(B / 2)
			B = B / 2
		for i in R1:
			for p in R2:
				if i == p:
					C += 1
		return C