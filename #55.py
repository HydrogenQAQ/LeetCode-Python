# Author: Jin


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        def path(num, index):
            if num + nums[num] >= index:
                l.append(True)
            elif nums[num] == 0:
                l.append(False)
            else:
                for i in range(num + 1, num + nums[num] + 1):
                    path(i, index)
        l = []
        path(0, len(nums) - 1)
        if True in l:
            return True
        else:
            return False

s = Solution()
l = [2,0,0]
print(s.canJump(l))
