# Author: Jin


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum, l = nums[0], 0
        for n in nums:
            l = max(n, n + l)
            maxNum = max(l, maxNum)
        return maxNum

s = Solution()
array = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(array))