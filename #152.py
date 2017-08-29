_author_ = 'Jin'


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum, minNum = nums[0], nums[0]
        res = nums[0]
        for x in nums[1:]:
            a = maxNum * x
            b = minNum * x
            maxNum = max(x, max(a, b))
            minNum = min(min(a, b), x)
            res = max(res, maxNum)
        return res

s = Solution()
L = [-2, 3, -4, -3]
print(s.maxProduct(L))