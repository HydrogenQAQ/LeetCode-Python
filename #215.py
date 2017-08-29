# -*- coding: utf-8 -*-

"""
@author: Jinqf
@file: #215
@time: 2017/8/28 17:43
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k - 1]
l = [1, 3, 54, 4, 23, 32, 12]
s = Solution()
print(s.findKthLargest(l, 2))