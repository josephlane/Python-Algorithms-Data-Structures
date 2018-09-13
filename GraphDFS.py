import sys

t = 1

balanced = True
ob = ['{','(','[']
cb = ['}', ')', ']']
for a0 in xrange(t): 
    s = '{[()]}'
    
    s1 = []
    s2 = []
   
    if s[0] not in ob or len(s) % 2 != 0:
        balanced = False
    else:
        for x in s:    
            if x in ob:
                s1.append(x)
            else:
                s2.append(x)
                
        while s1:
            if s1.pop() != s2.pop(0):
                balanced = False
                break
     
    if balanced:
        print "YES"
    else:
        print "NO"
        else:
            s2.append(char)
    for i in range(0, len(s)):
        c1 = s1.pop()
        c2 = s2.pop(0)
        if c1 != c2:
            balanced = False
            break
            
    if balanced:
        print "YES"
    else:
        print "NO"
