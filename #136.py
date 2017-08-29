# Author: Jin


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        for i in range(1, len(nums), 2):
            res -= nums[i]
        return res

s = Solution()
l = [1, 1, 2, 3, 5, 3, 5]
print(s.singleNumber(l))