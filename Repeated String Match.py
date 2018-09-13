def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    
    if len(A) > len(B) and B in A:
        return 0
    
    count = 1
    
    C = A

    for i in range(1, 10000):
        A += C
        count += 1
        if len(A) > len(B) and B in A:
            print B, A
            found = True
            break
            
    if found:
        return count
    else:
        return -1

print repeatedStringMatch("a", "aa")

print repeatedStringMatch("abcd", "cdabcdab")
