# Author: Jin


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        关键点在于如果左边i的比右边j小，那么i-j之间一定是有序的
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            # 如果当前l-r是两个有序序列的话
            else:
                if nums[m] >= nums[l]:
                    if nums[l] <= target <= nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[m] <= target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        if l == r and nums[l] == target:
            return l
        else:
            return -1

s = Solution()
l = [3, 1]
target = 1
print(s.search(l, target))