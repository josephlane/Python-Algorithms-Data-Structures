class TheBlackJackDivTwo:
	def score(self, cards):
		total = 0
		for card in list(cards):
			if card[0] in ["T", "J", "Q", "K"]:
				total += 10
			elif card[0] == "A":
				total += 11
			else:
				total += int(card[0])
		return total

s = TheBlackJackDivTwo()
print s.score(("4S", "7D"))