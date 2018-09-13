def migratoryBirds(n, ar):
    t1 = {}
    for i in ar:
        if i in t1:
            t1[i] += 1
        else:
            t1[i] = 1
    t2 = sorted(t1.items(), key=lambda(k, v): (-v, k))
    return t2
n = 6
ar = [1,4,4,5,5,3]
result = migratoryBirds(n, ar)
print(result)

