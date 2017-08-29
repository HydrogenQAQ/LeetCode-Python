# Author: Jin


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    temp.append((i, j))
        for x in temp:
            for j in range(len(matrix[0])):
                matrix[x[0]][j] = 0
            for i in range(len(matrix)):
                matrix[i][x[1]] = 0
        return matrix

s = Solution()
m = [[1, 0, 2],
     [2, 3, 4]]
print(s.setZeroes(m))
