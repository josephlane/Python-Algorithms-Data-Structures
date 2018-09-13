from nose.tools import assert_equal

class AnagramTest:

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi         man'), True)
        print 'ALL TEST PASSED'


class Anagram:

    def valid(self, v1, v2):

        v1 = v1.replace(' ', '').lower()
        v2 = v2.replace(' ', '').lower()

        if len(v1) != len(v2):
            return False

        d = {}

        valid = True

        for char in v1:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        for char in v2:
            if char in d:
                d[char] -= 1

        for val in d.values():
            if val != 0:
                valid = False
                break

        return valid
                
        

a = Anagram()

anagram = AnagramTest()
anagram.test(a.valid)
