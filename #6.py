# Author: Jin


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i, cnt = 0, 0
        ret = ''
        while s[i]:
            if i > len(s):
               i = cnt
            for i in range(i, len(s)):
                ret += s[i]
                i += (2 * numRows - 2)



ss = Solution()
words = input()
num = int(input())
print(ss.convert(words, num))

# if numRows == 1:
#     return s
# zig, temp = [], []
# i, cnt = 0, 0
# while i < len(s):
#     if cnt == 0:
#         if i + numRows > len(s):
#             for i in range(i, len(s)):
#                 temp.append(s[i])
#             for xx in range(i + numRows - len(s)):
#                 temp.append('')
#             i = len(s) + 1
#         else:
#             for i in range(i, i + numRows):
#                 temp.append(s[i])
#             cnt = numRows - 2
#             i += 1
#     else:
#         for t in range(numRows):
#             if t == cnt:
#                 temp.append(s[i])
#             else:
#                 temp.append('')
#         cnt -= 1
#         i += 1
#     zig.append(temp)
#     temp = []
# ret = ''
# for j in range(numRows):
#     for k in range(len(zig)):
#         ret += zig[k][j]
# return ret