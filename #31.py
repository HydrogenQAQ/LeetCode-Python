# Author: Jin


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        isA = True
        for c in range(-1, -1 - len(nums), -1):
            for j in range(c - 1, -1 - len(nums), -1):
                if nums[c] > nums[j]:
                    temp = nums[c]
                    nums[c] = nums[j]
                    nums[j] = temp
                    for i in range(len(nums) + j + 1, len(nums) - 1):
                        for k in range(i + 1, len(nums)):
                            if nums[i] > nums[k]:
                                temp = nums[i]
                                nums[i] = nums[k]
                                nums[k] = temp
                    # sequence = nums[j + 1:]
                    # sequence.sort()
                    # nums = nums[:j + 1] + sequence
                    isA = False
                    break
                else:
                    continue
            if isA is False:
                break
        if isA is True:
            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    if nums[i] > nums[j]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
        return nums


s = Solution()
l = [3, 2, 1]
print(s.nextPermutation(l))