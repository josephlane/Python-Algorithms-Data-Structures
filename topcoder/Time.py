class Time:

	def whatTime(self, seconds):
		hours = (seconds / 3600)
		remainder = (seconds % 3600)
		minutes = (remainder / 60)
		remainder2 = (remainder % 60)
		seconds = (remainder2 / 1)
		return str(hours) + ":" + str(minutes) + ":" + str(seconds)
		
	def whatTime2(self, seconds):
		return ":".join(
							(
								str(int(seconds/3600)), str(int(seconds/60) % 60), str(int(seconds%60))
							)
						)

s = Time()
print s.whatTime2(0)