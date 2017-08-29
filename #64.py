# Author: Jin


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    res[i][j] = res[i][j - 1] + grid[i][j]
                elif j == 0:
                    res[i][j] = res[i - 1][j] + grid[i][j]
                else:
                    res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[-1][-1]

s = Solution()
g = [[1, 2, 5],
     [3, 2, 1]]
print(s.minPathSum(g))