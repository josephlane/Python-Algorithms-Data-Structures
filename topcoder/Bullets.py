import re

class Bullets:
    def match(self, guns, bullet):
		guns = list(guns)
		bullet = re.split('(\s+)', bullet)
		bullet.sort()
		bullet = " ".join(bullet)
		print "Bullet:" + bullet
		for i in range(len(guns)):
			gun = re.split('(\s+)',guns[i])
			print gun
			gun.sort()
			print gun
			gun = " ".join(gun)
			print "Gun:{%s}:{%s}" % (i, gun)
			if gun == bullet:
				return i
		return -1            

b = Bullets()
print b.match({"||| |","| | || "}, "|||| ")