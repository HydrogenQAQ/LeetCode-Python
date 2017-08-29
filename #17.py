# Author: Jin


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dd = {"0": "0", "1": "1", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
              "9": "wxyz"}
        res = [""]
        for digit in digits:
            tempStr = []
            for s in dd[digit]:
                for string in res:
                    tempStr.append(string + s)
            res = tempStr
        return res


ss = Solution()
s = input()
print(ss.letterCombinations(s))