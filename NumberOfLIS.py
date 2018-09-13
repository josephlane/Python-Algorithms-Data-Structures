def nLIS(x):

    if len(x) == 0:
        return 0

    if len(x) == 1:
        return 1

    memo = [[1,1] for i in range(len(x))]

    for j in range(0, len(x)):
        for i in range(j+1, len(x)):
            if x[j] < x[i]:
                memo[i][0] = max(memo[j][0] + 1, memo[i][0])
                memo[i][1] += 1

    print memo
                


x = [1,-1,6,7,-3,4]

nLIS(x)
