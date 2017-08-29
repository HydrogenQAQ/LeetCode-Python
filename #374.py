# Author: Jin

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0


def guess(num):
    if num == 1:
        return 0
    elif num < 1:
        return 1
    else:
        return -1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            isA = guess(m)
            if isA == 1:
                l = m + 1
            elif isA == -1:
                r = m - 1
            else:
                return m


s = Solution()
n = int(input())
print(s.guessNumber(n))
