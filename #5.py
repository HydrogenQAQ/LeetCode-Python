# Author: Jin


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret, i = '', 0
        while True:
            max_len = len(ret)
            if i >= len(s) - max_len:
                break
            for j in range(i + max_len, len(s)):
                temp = s[i:j + 1]
                if (j + 1 - i) > max_len and (temp == temp[::-1]):
                    ret = temp
            i += 1
        return ret


ss = Solution()
words = input()
print(ss.longestPalindrome(words))

