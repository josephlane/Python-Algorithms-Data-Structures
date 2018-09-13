import math

class DegreesToRadians:
	def convertToRadians(self, degrees, minutes, seconds):
		return math.radians(degrees + (minutes / 60.0) + (seconds / 3600.0))

s = DegreesToRadians()
print s.convertToRadians(359, 59, 59)