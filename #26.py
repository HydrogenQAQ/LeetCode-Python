# Author: Jin


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if i + 1 >= len(nums):
                break
            elif nums[i] == nums[i + 1]:
                while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                    nums.pop(i)
        return len(nums)


s = Solution()
nums = [1, 1, 2, 2, 3, 4]
s.removeDuplicates(nums)
for num in nums:
    print(num)