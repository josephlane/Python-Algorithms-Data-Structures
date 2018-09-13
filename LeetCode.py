class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = nums[0]
        maxPos = 0
        valid = True

        for mIndex, mMax in enumerate(nums):

            if mMax > maxNum:
                maxNum = mMax
                maxPos = mIndex

                                    
        for i, num in enumerate(nums):
            if maxNum != num:
                if num * 2 > maxNum:
                    valid = False
        
        if valid:
            return maxPos
        else:
            return -1


s = Solution()

print s.dominantIndex([3, 6, 1, 0])
print s.dominantIndex([1, 2, 3, 4])
print s.dominantIndex([0])
print s.dominantIndex([2,3])
