class MostProfitable:
	def bestItem(self, costs, prices, sales, items):
		maxVal = -1
		maxPos = -1
		costs, prices, sales, items = list(costs), list(prices), list(sales), list(items)
		print items
		for i in xrange(len(costs)):
			cost = costs[i]
			price = prices[i]
			sale = sales[i]
			name = items[i]
			profit = (price - cost) * sale
			if profit > 0 and profit > maxVal:
				maxVal = profit
				maxPos = i

		if maxVal != -1:
			return items[maxPos]
		else:
			return ""


costs = (100,120,150,1000)
prices = (110,110,200,2000)
sales = (20,100,50,3)
items = ("Video Card","256M Mem","CPU/Mobo combo","Complete machine")

# costs = str(100)
# prices = str(100)
# sales = str(134)

#items = str(("Service, at costs"))


p = MostProfitable()
print p.bestItem(costs, prices, sales, items)
