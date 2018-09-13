def shortestPalindrome(s):
    for i in xrange(len(s) - 1, 0, -1):
        p.append(x[i])
        if len(p) == len(x[1:]):
            found = True
            break
    if found:
        return "".join(p) + "".join(x)
    else:
        return "None"

print shortestPalindrome("RUN")