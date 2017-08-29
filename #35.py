# Author: Jin

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target < nums[0]:
            return 0
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            elif nums[i] < target < nums[i + 1]:
                return i + 1
        return len(nums) - 1 if nums[-1] == target else len(nums)

s = Solution()
nums = [1, 2, 3]
t = 1
print(s.searchInsert(nums, t))