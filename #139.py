# Author: Jin


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ans = []

        def wordFind(s, wordDict):
            if len(s) == 0:
                ans.append(True)
                return True
            if len(s) == 1 and s in wordDict:
                ans.append(True)
                return
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict and wordFind(s[i:], wordDict):
                    return
        wordFind(s, wordDict)
        if True in ans:
            return True
        else:
            return False

s = Solution()
l = ['car', 'ca', 'rs', 'bbbb']
word = input()
print(s.wordBreak(word, l))
