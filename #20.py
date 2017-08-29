# Author: Jin


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mdict = {'(': 1, '[': 2, '{': 3, ')': 4, ']': 5, '}': 6}
        temp = []
        for i in range(len(s)):
            if mdict[s[i]] <= 3:
                temp.append(s[i])
            # 当栈中有元素且刚入栈的元素为栈顶元素的补才将栈顶弹出栈
            elif mdict[s[i]] >= 3 and len(temp) > 0 and mdict[s[i]] - mdict[temp[-1]] == 3:
                temp.pop()
            else:
                return False
        return len(temp) == 0


ss = Solution()
words = input()
print(ss.isValid(words))