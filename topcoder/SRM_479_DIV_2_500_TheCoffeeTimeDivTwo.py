class TheCoffeeTimeDivTwo:
	
	def find(self, n, tea):	

		fill, seconds, drink = 0, 0, "Tea"
		
		for i in range(1, n+1):
			if i in tea:
				fill = 0 if drink == "Coffee" else fill
				seconds, fill = calculateSeconds(drink, fill, i, seconds, tea, n)
				drink = "Tea"
			else:
				fill = 0 if drink == "Tea" else fill
				seconds, fill = calculateSeconds(drink, fill, i, seconds, tea, n)
				drink = "Coffee"
			#print "Current Iteration: %d -- Total Seconds: %d Current Fill: %d" % (i, seconds, fill)
		return seconds

def calculateSeconds(drink, fill, iteration, seconds, tea, n):
	if fill == 0: #Empty Cup
		#print "---The Flask is empty"
		if iteration == 1: #Starting at Drink Machine
			seconds += 47 + iteration + 4 #(Fill up flask, go to customer, poor drink)
			#print "Started at drink machine(iteration=%d): Total seconds = %d" %(iteration,seconds)
		elif iteration == n: #Last customer to be served
			seconds += 1 + 47 + iteration + 4 + iteration #(Go to customer, Serve customer, go back to drink machine)
			#print "Served Last Customer(iteration=%d): Total Seconds = %d" %(iteration,seconds)
		else: #Next customer in line
			seconds += iteration + 47 + iteration + 4
			#print "Served Next Customer(iteration=%d): Total Seconds = %d" %(iteration,seconds)

		fill = 6
	else: #cup is not empty
		#print "---The Flask is NOT empty"
		if iteration == n:
			seconds += 1 + 4 + iteration
			#print "Served Last Customer(iteration=%d): Total Seconds = %d" %(iteration,seconds)
		else:
			seconds += 1 + 4
			#print "Served Next Customer(iteration=%d): Total Seconds = %d" %(iteration,seconds)
		fill -= 1
	return [seconds, fill]

s = TheCoffeeTimeDivTwo()
print s.find(2, {1})
print s.find(2, {2,1})
print s.find(15, {1, 2, 3, 4, 5, 6, 7})
print s.find(47, {1, 10, 6, 2, 4})