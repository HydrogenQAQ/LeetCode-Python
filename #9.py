# Author: Jin


class Solution(object):
    def isPalindrome(self, x):
        """
        判断数字是否回文(正序倒序一样)
        :type x: int
        :rtype: bool
        """
        # 负数不是回文数
        if x < 0:
            return False
        cnt, n = 0, x
        while n:
            n //= 10
            cnt += 1
        left, right = 10 ** cnt, 10
        while left >= right:
            temp = x // left
            top = x // (left / 10) - temp * 10
            low = (x % right) // (right / 10)
            left /= 10
            right *= 10
            if top != low:
                return False
        return True


s = Solution()
num = int(input())
print(s.isPalindrome(num))