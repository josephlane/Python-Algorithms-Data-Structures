class FallingSand:
	def simulate(self, board):
		board = map(list, board)
		for i in range(len(board)):
			for i in range(len(board)-1, 0, -1):
				for j in range(len(board[0])):
					if board[i][j] == "." and board[i-1][j]:
						board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
		return tuple("".join(i) for i in board)

a = ("ooo","...",".x.", ".x.")


b = FallingSand()
print b.simulate(a)


