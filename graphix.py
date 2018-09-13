from collections import deque
h = 400
l = 600

class grafixMask:
	def sortedAreas(self, rectangles):
		re = []

		#INITIALIZE  MATRIX TO BE ALL FALSE
		grid = [[False for x in xrange(l)] for y in xrange(h)]

		#this code initializes 
		for rectangle in rectangles:
			x1,y1,x2,y2 = map(int, rectangle.split())
			for i in xrange(x1, x2+1):
				for j in xrange(y1, y2+1):
					grid[i][j] = True	

		#if position is not visited, visit position
		for x in xrange(h):
			for y in xrange(l):
				if grid[x][y] == False:
					#print x, y
					re.append(self.dfs(x, y, grid))
		
		return sorted(tuple(re))

	def dfs(self, x, y, grid):
		result = 0

                d = deque((x,y))
                
                x,y = deque.popleft()

		while d: #NOT EMPTY
			x, y = d.popleft()	#get item from stack	

			if x < 0 or x >= h: #check bounds of x
				continue
			
			if y < 0 or y >= l: #check bounds of y
				continue

			if grid[x][y]: #if already visited, skip
				continue
			
			grid[x][y] = True #mark as visited
	
			result += 1 #since we marked this as visited, track it

			#visit every adjacent node to see if it's visited or not
			d.appendleft((x - 1, y))
			d.appendleft((x + 1, y))		
			d.appendleft((x, y - 1))
			d.appendleft((x, y + 1))

		return result
