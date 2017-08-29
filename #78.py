# Author: Jin


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy

        def sub(num):
            temp = copy.deepcopy(res)
            if len(res) == 0:
                res.append([num])
            else:
                for x in temp:
                    x.append(num)
                    res.append(x)
                res.append([num])
        res = []
        for i in range(len(nums)):
            sub(nums[i])
        res.append([])
        return res


s = Solution()
l = [1]
print(s.subsets(l))