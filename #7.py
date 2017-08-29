# Author: Jin

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isA = True
        num_list = []
        # 若为负数先转化为正数
        if x < 0:
            isA = False
            x = abs(x)
        while x != 0:
            num_list.append(x % 10)
            # 整除
            x //= 10
        ret = 0
        for i in range(len(num_list)):
            ret = ret * 10 + num_list[i]
        # 溢出返回0,注意判断的是输出
        if ret > 2 ** 31 or ret < -2 ** 31:
            return 0
        elif isA is False:
            ret = -ret
        return ret


x = int(input())
s = Solution()
print(s.reverse(x))