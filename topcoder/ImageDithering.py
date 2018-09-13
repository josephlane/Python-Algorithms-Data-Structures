
class ImageDithering:
	def count(self, dithered, screen):
		a = "".join(screen)
		count = 0
		for i in dithered:
			count += a.count(i)
		return count

a = ("AAAAAAAA",
 "ABWBWBWA",
 "AWBWBWBA",
 "ABWBWBWA",
 "AWBWBWBA",
 "AAAAAAAA")

c = "BW"

b = ImageDithering()
print b.count(c, a)
