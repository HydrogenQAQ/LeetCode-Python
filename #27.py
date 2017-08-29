# Author: Jin


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        for n in nums:
            if n != val:
                nums[cnt] = n
                cnt += 1
        for i in range(cnt, len(nums)):
            nums.pop()
        return cnt

s = Solution()
l = [3, 2, 2, 3]
print(s.removeElement(l, 3))