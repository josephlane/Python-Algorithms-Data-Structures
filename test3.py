a = [0, 1, 2, 3, 4]

def iter(i=0):
	if i <= a[len(a) -1]:
		print a[i]
		iter(i+1)
iter()


a = {}

print a