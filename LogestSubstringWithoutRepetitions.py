def ls(x):
    m = [1 for s in range(len(x))]
    u = set()
    for j in range(len(x)):
        for i in range(j+1, len(x)):
            if x[j] not in u and x[j] != x[i]:
                m[j] = max(m[j] + 1, m[i])
                u.add(x[j])
    print m

def ls2(x):
    v = set()
    r = ""
    for k in range(1, len(x)-1):
        if x[k] not in v:
            r = r + x[k]
            v.add(x[k])

    return len(r)

print ls2("pwwkew")
