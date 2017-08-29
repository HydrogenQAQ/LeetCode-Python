# Author: Jin

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        length = start = 0
        for i in range(len(s)):
            if s[i] in dict1 and start <= dict1[s[i]]:
                start = dict1[s[i]] + 1
            else:
                length = max(length, i - start + 1)
            dict1[s[i]] = i
        return length

ss = Solution()
words = str(input())
print(ss.lengthOfLongestSubstring(words))