
#Note, x must be sorted in order for these function to work
def isUnique(x):
	unique = True

	for i in range(1, len(x)):
		if x[i-1] == x[i]:
			unique = False

	return unique


x = [4,5,2,6,9,2]

x.sort()

print isUnique(x)

	