# Author: Jin


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxPrice, buy = 0, prices[0]
        for i in range(1, len(prices)):
            buy = min(prices[i], buy)
            maxPrice = max(prices[i] - buy, maxPrice)
        return maxPrice

s = Solution()
l = [7]
print(s.maxProfit(l))