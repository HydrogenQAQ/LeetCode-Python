_author_ = 'Jin'


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 0
            numDict[num] += 1
        for key in numDict:
            if numDict[key] > len(nums) // 2:
                return key


s = Solution()
l = [1, 2, 3, 3, 4]
print(s.majorityElement(l))