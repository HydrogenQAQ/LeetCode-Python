# Author: Jin


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans, res = [], {}
        for s in strs:
            temp = list(s)
            temp.sort()
            ans.append("".join(temp))
        for i in range(len(ans)):
            if ans[i] not in res:
                res[ans[i]] = []
            res[ans[i]].append(strs[i])
        ret = []
        for key in res:
            ret.append(res[key])
        return ret

s = Solution()
ans = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(ans))
