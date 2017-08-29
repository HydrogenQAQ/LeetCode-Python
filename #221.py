# -*- coding: utf-8 -*-

"""
@author: Jinqf
@file: #221
@time: 2017/8/28 20:53
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        numMax = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = '1'
                    if i > 0 and j > 0:
                        dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                if dp[i][j] > numMax:
                    numMax = dp[i][j]
        return numMax ** 2


s = Solution()
l = ['0']
print(s.maximalSquare(l))