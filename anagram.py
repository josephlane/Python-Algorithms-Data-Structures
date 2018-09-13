def anagram(s, t):

    #base cases

    if len(s) == 0 and len(t) == 0:
        return True 

    if len(s) != len(t):
        return False

    valid = True

    s = sorted(s)
    t = sorted(t)
    
    for i in range(0, len(s)):
        if s[i] != t[i]:
            return False

    return True


print anagram(s, t)
