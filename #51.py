# Author: Jin


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def conflit(state, nextX):
            nextY = len(state)
            for i in range(len(state)):
                if abs(state[i] - nextX) in (0, nextY - i):
                    return True
            return False

        def queen(n, state):
            for i in range(n):
                if not conflit(state, i):
                    if len(state) == n - 1:
                        yield (i,)
                    else:
                        for result in queen(n, state + (i,)):
                            yield (i,) + result
        ret = []
        for x in queen(n, state=()):
            res = []
            for i in range(len(x)):
                temp = str('.' * x[i] + 'Q' + '.' * (len(x) - x[i] - 1))
                res.append(temp)
            ret.append(res)
        return ret

s = Solution()
n = int(input())
print(s.solveNQueens(n))
