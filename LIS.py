
def LIS(x):

    if len(x) == 1:
        return 1

    if len(x) == 0:
        return 0

    memo = [1 for i in range(0, len(x))]
    

    for j in range(0, len(x)):
        for i in range(j + 1, len(x)):
            if x[j] < x[i]:
                memo[i] = max(memo[j] + 1, memo[i])

    #return max(memo)
    return sum(s == max(memo) for s in memo)


x = [3,4,-1,0,6,2,3]
print LIS(x)
