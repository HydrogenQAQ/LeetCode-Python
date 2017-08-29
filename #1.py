# Author: Jin

"""Given an array of integers, return indices of the two numbers such
that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        更优秀的解 O（n）
        tmp_num = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp_num:
                # here do not need to deal with the condition i = target-i
                return (tmp_num[target-nums[i]], i)
            else:
                tmp_num[nums[i]] = i
        return (-1, -1)  """

        result = []
        isA = True
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    isA = False
                    break
            if isA is False:
                break
        return result

nums = []
a = input()
for i in a.split(','):
    nums.append(int(i))
target = int(input())
solution = Solution()
print(solution.twoSum(nums, target))