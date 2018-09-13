from itertools import product

def getPerms(t):
    perms = [p for p in product([0,1,-1], repeat=t)]
    return perms

def answer(t, n):
    up = 0
    perms = getPerms(t)
    for perm in perms:
        total = 0
        validPerm = True
        for value in perm:
            if (perm.index(value) > n-2) and value == -1:
                validPerm = False
            else:
                total += value
        if perm[0] != -1 and (n-total) == 1 and perm[len(perm) -1] != -1 and validPerm:              
            up+=1
    return up

def answer2(t, n):
    up = 0
    for perm in product([0,1,-1], repeat=t):
        if perm[0] == -1 or perm[len(perm)-1] == -1:
            continue
        total = 0
        validPerm = True
        for value in perm:
            if (perm.index(value) > n-2) and value == -1:
                validPerm = False
            else:
                total += value
        if (n-total) == 1 and validPerm:              
            up+=1
    return up % 123454321


print answer2(67, 2)
        
