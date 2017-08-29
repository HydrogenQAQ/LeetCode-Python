# Author: Jin
"""
AC 代码：
l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s):
            # 判断是字母或数字
            if s[i].isalnum():
                i += 1
                if i == len(s):
                    break
                else:
                    continue
            else:
                s = s[:i] + s[i + 1:]
        return s.lower() == s.lower()[::-1]

ss = Solution()
words = input()
print(ss.isPalindrome(words))

