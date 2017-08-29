# Author: Jin


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colorCount = [0] * 3
        for color in nums:
            colorCount[color] += 1
        for i in range(len(nums)):
            if i < colorCount[0]:
                nums[i] = 0
            elif colorCount[0] <= i < (colorCount[0] + colorCount[1]):
                nums[i] = 1
            else:
                nums[i] = 2
        return

s = Solution()
l = [1, 2, 2, 0, 0, 2]
print(s.sortColors(l))