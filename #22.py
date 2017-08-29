# Author: Jin


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(vector, left, right, temp):
            if left == 0 and right == 0:
                vector.append(temp)
            if left > 0:
                generate(vector, left - 1, right, temp + '(')
            if right > 0 and right > left:
                generate(vector, left, right - 1, temp + ')')
        ret = []
        generate(ret, n, n, "")
        return ret

s = Solution()
num = int(input())
print(list(s.generateParenthesis(num)))