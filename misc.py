
#Note, x must be sorted in order for these function to work
def isUnique(x):
	unique = True
	for i in range(1, len(x)):
		if x[i-1] == x[i]:
			unique = False

	return unique

#Note, takes up more space O(n^2)
def isUnique2(x):
	unique = True
	for i in range(0, len(x)):
		for s in range(i+1, len(x)):
			if x[i] == x[s]:
				unique = False
	return unique

def test(x):
	if x == None: return

	if 1==1:
		return "YES"

x = "ZSXDCFV"
x = None
print test(x)



	