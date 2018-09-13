#Uses the gready method
def minCoins(n, coins, count):

    if n == 0:
        return count

    if len(coins) > 0:

        coin = coins[len(coins)-1]

        if coin <= n:
            count += (n / coin)
            n = n % coin
            
        return minCoins(n, coins[:-1], count)

    else:
        return 'Error: Invalid change'

def num_of_ways(change, coins):

    if change == 0:
        return 1
    t = []
    for coin in coins:
        if change >= coin:
            t.append(num_of_ways(change-coin, coins))
            print t
    return len(t)

num_of_ways(4, [1,2,3,4])

#coins = [1,5,10, 25]
#n = 45
#
#print minCoins(n, coins, 0)
#
#coins = [1,5,10, 25]
#n = 23
#
#print minCoins(n, coins, 0)
#
#coins = [1,5,10,21,25]
#n = 63
#
#print minCoins(n, coins, 0)
#

    
