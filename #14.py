# Author: Jin

"""
Write a function to find the longest common prefix string amongst an array of strings.
返回最长公共前缀
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret, cnt = '', 0
        if not strs:
            return ret
        elif len(strs) == 1:
            return strs[0]
        while True:
            for i in range(len(strs) - 1):
                if len(strs[i + 1]) <= cnt or len(strs[i]) <= cnt or strs[i][cnt] != strs[i + 1][cnt]:
                    return ret
            ret += strs[0][cnt]
            cnt += 1

s = Solution()
strs = [""]
print(s.longestCommonPrefix(strs))
