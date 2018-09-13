h = 400
l = 600

class grafixMask:

  def sortedAreas(self, rectangles):
  
    finalResult = []
    
    #INITIALIZE  MATRIX TO BE ALL FALSE
    grid = [[False for x in range(l)] for y in range(h)]

    for rectangle in rectangles:
      x1,y1,x2,y2 = map(int, rectangle.split())

      for x in range(x1, x2+1):
        for y in range(y1, y2+1):
          grid[x][y] = True

    #if position is not visited, visit position
    for x in range(h):
      for y in range(l):
        if grid[x][y] == False:
          xx = self.dfs(x, y, grid)
          finalResult.append(xx)

    return tuple(sorted(finalResult))

  def dfs(self, x, y, grid):
    
    result = 0

    stack = [(x,y)]

    #while stack is not empty
    while stack:

      #get cordinates from stack
      x, y = stack.pop() 

      #check bounds of x
      if x < 0 or x >= h: 
        continue
      #check bounds of y
      if y < 0 or y >= l: 
        continue
      #if already visited, skip
      if grid[x][y] == True: 
        continue

      #mark as visited
      grid[x][y] = True
      
      #since we marked this as visited, track it
      result += 1 

      #due to memory constraints, loop through and append to stack so that each object is recycled 
      #and used by the next process. Do not append to stack all at once. 
      #This code adds every adjacent node to thestack for review
      stack.append((x - 1, y))     
      stack.append((x + 1, y))     
      stack.append((x, y - 1))      
      stack.append((x, y + 1))
          
    return result

a = {"50 300 199 300", "201 300 350 300", "200 50 200 299", "200 301 200 550"}
#0 Returns: { 116800,  116800 }

z = grafixMask()
#ab = z.sortedAreas(a)
#print ab
print(z.sortedAreas(a))
#ab = z.sortedAreas(c)
#print ab
#ab = z.sortedAreas(d)
#print ab





