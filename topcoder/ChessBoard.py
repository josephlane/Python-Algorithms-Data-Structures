class Chessboard:
	def changeNotation(self, cell):
		p = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
		c = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h"}
		if cell[0] not in p:
			cell = int(cell)
			row_num = (cell / 8) + 1 if cell > 8 else 1
			col_num = (cell % 8) if cell > 8 else (cell)
			return c[col_num] + str(row_num)
		else:
			col_num = int(p[cell[0]])
			row_num = int(cell[1]) -1
			return (row_num * 8) + col_num if row_num > 1 else col_num

x = Chessboard()
print x.changeNotation("h8")