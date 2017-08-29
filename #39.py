# Author: Jin


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combination(candidates, target, temp, index, res):
            if target < 0:
                return
            if target == 0:
                res.append(temp)
                return
            for i in range(index, len(candidates)):
                combination(candidates, target - candidates[i], temp + [candidates[i]], i, res)

        candidates.sort()
        temp, res = [], []
        combination(candidates, target, temp, 0, res)
        return res


s = Solution()
l = [2, 3, 6, 7]
t = 7
print(s.combinationSum(l, t))