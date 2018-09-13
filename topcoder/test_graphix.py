class grafixMask(object):

    def sortedAreas(self, rectangles):
        h,w=400,600
        grid = [[False for j in range(w)] for i in range(h)]

        for s in rectangles:
            x1,y1,x2,y2 = map(int, s.split())

            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] = True

        res = []
        moves = ((0,1),(0,-1),(1,0),(-1,0))

        def dfs(x,y):
            r=0
            stack = [(x,y)]

            while stack:
                x,y = stack.pop()
                if grid[x][y] == False:
                    r+=1 
                    grid[x][y] = True
                else:
                    continue

                for mx,my in moves:
                    nx,ny=x+mx,y+my

                    if 0<=nx and nx<h and 0 <=ny and ny<w and grid[nx][ny] == False:
                        stack.append((nx,ny))

            return r

        for i in range(h):
            for j in range(w):
                if grid[i][j] == False:
                    res.append(dfs(i,j))
        res.sort()
        return res

a = ("50 300 199 300", "201 300 350 300", "200 50 200 299", "200 301 200 550")
xx = grafixMask()
z = xx.sortedAreas(a)
print z