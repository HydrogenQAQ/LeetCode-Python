# Author: Jin


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        for i in range(len(nums) - 3):
            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]) > target:
                break
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp < target:
                        l += 1
                    elif temp > target:
                        r -= 1
                    else:
                        indexs = [nums[i], nums[j], nums[l], nums[r]]
                        if indexs not in ret:
                            ret.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return ret


s = Solution()
nums = [-3, -2, -1, 0, 0, 1, 2, 3, 0]
target = int(input())
print(s.fourSum(nums, target))