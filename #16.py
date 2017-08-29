# Author: Jin

"""
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sums = nums[i] + nums[l] + nums[r]
                diff = sums - target
                if diff == 0:
                    return target
                elif diff < 0:
                    result.append(diff)
                    l += 1
                else:
                    result.append(diff)
                    r -= 1
        result.sort()
        if result[0] > 0:
            return target + result[0]
        elif result[-1] < 0:
            return target + result[-1]
        else:
            for i in range(len(result)):
                if result[i] < 0 < result[i + 1]:
                    if abs(result[i]) < result[i + 1]:
                        return target + result[i]
                    else:
                        return target + result[i + 1]
a = input()
array = []
for i in a.split(','):
    array.append(int(i))
n = int(input())
s = Solution()
print(s.threeSumClosest(array, n))
