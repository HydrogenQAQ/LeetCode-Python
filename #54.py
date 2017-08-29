# Author: Jin


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return matrix
        ret = []
        i, j, w, cnt = 0, 0, 1, 1
        ret.append(matrix[i][j])
        isL, isR, isT, isB = False, True, False, False
        while True:
            if cnt == len(matrix) * len(matrix[0]):
                break
            while isR and (cnt != len(matrix) * len(matrix[0])):
                if j == len(matrix[0]) - w:
                    isR = False
                    isB = True
                    break
                j += 1
                ret.append(matrix[i][j])
                cnt += 1
            while isB and (cnt != len(matrix) * len(matrix[0])):
                i += 1
                if i == len(matrix) - w:
                    isB = False
                    isL = True
                ret.append(matrix[i][j])
                cnt += 1
            while isL and (cnt != len(matrix) * len(matrix[0])):
                j -= 1
                if j == w - 1:
                    isL = False
                    isT = True
                    w += 1
                ret.append(matrix[i][j])
                cnt += 1
            while isT and (cnt != len(matrix) * len(matrix[0])):
                i -= 1
                if i == w - 1:
                    isT = False
                    isR = True
                ret.append(matrix[i][j])
                cnt += 1
        return ret

s = Solution()
m = [[1]]
print(s.spiralOrder(m))