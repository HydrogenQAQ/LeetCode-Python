# Author: Jin


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combination(candidates, target, path, index):
            if target < 0:
                return
            if target == 0:
                res.append(path)
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                combination(candidates, target - candidates[i], path + [candidates[i]], i + 1)

        temp, res = [], []
        candidates.sort()
        combination(candidates, target, temp, 0)
        return res

s = Solution()
l = [10, 1, 2, 7, 1, 6, 5]
target = 8
print(s.combinationSum2(l, target))