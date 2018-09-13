class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        
        return max(dp)

    def lengthOfLIS2(self, nums):
        
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = 0
        
        return max(dp)
        


s = Solution()
#a = s.lengthOfLIS([1,3,5,4,7])
#b = s.lengthOfLIS2([1,3,5,4,7])
b = s.lengthOfLIS2([1,2,5,0,2,3,8,9])
print b



