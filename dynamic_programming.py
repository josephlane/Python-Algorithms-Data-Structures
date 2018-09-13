#------------------------------
#DYNAMIC PROGRAMMING EXAMPLES
#DATE: 9/21/2017 by Joseph Lane
#------------------------------

#CLASSIC FIBONACCI SEQUENCE
#FIB(3) = FIB(2) + FIB(1)

#NONE MEMOIZATION

import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#WITH MEMOIZATION

def fibm(n):
    
    #initialize storage
    memo = [-1 for i in range(0, n)]

    #base case 1
    if n == 0:
        return 0

    #base case 2
    if n == 1:
        return 1

    #store value if it doesn't already exists in storage
    if memo[n-1] == -1:
        memo[n-1] = fib(n-1) + fib(n-2)
        
    return memo[n-1]

def numOfPaths2(row, col, grid):
       
    #base case
    if len(grid) == 0:
        return 0
    
    if row == len(grid) -1 and col == len(grid[0]) - 1:
        return 1

    #validation of position

    if not validPath(row, col, grid):
        return 0

    return numOfPaths(row + 1, col, grid, memo) + numOfPaths(row, col + 1, grid, memo)

def numOfPaths(row, col, grid, memo):
       
    #base case
    if len(grid) == 0:
        return 0
    
    if row == len(grid) -1 and col == len(grid[0]) - 1:
        return 1

    #validation of position

    if not validPath(row, col, grid):
        return 0

    #if calculating value for first time, save it in storage
    if memo[row][col] == -1:
        memo[row][col] = numOfPaths(row + 1, col, grid, memo) + numOfPaths(row, col + 1, grid, memo)

    return memo[row][col]
    
def validPath(row, col, grid):

    #valid row
    if row < 0 or row >= len(grid):
        return False
        

    #validate col
    if col < 0 or col >= len(grid[0]):
        return False
    
    if grid[row][col] == "X":
        return False

    return True

    
#print fib(30)
#print fibm(30)

rows = 100
columns = 100

grid = [['' for col in range(0, columns)] for row in range(0, rows)]

memo = [[-1 for col in range(0, len(grid[0]))] for row in range(0, len(grid))]

t0 = time.time()

numOfPaths(0,0, grid, memo)

t1 = time.time()

print "Memoized solutions takes {0} time to complete".format(str(t1-t0))

t0 = time.time()

numOfPaths2(0,0, grid)

t1 = time.time()

print "Non-Memoized solutions takes {0} time to complete".format(str(t1-t0))
