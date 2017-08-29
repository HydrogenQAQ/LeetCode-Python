# Author: Jin


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA = (len(height) - 1) * min(height[0], height[-1])
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            if ((r - l) * min(height[l], height[r])) > maxA:
                maxA = (r - l) * min(height[l], height[r])
        return maxA


s = Solution()
l = [1, 1]
print(s.maxArea(l))