from nose.tools import assert_equal

class TestCompress:

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print 'ALL TEST CASES PASSED'


def compress(val):
    counts = {}

    for char in val:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return "".join(str(k) + str(v) for k,v in sorted(counts.iteritems()))


    

t = TestCompress()
t.test(compress)

