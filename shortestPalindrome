def shortestPalindrome(self, s):
    x = list(s)
    p = []
    found = False
    
    for i in xrange(len(x), 0, -1):
        p.append(x[i])
        if p == x:
            found = True
            break
    
    if found:
        return "".join(x) + "".join(p)
    else:
        return "None"

print shortestPalindrome("RUN")