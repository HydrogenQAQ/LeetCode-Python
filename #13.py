# Author: Jin

"""
罗马数字共有七个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)。
按照下面的规则可以表示任意正整数。

重复数次：一个罗马数字重复几次，就表示这个数的几倍。

右加左减：在一个较大的罗马数字的右边记上一个较小的罗马数字，表示大数字加小数字。
在一个较大的数字的左边记上一个较小的罗马数字，表示大数字减小数字。但是，左减不能跨越等级。
比如，99不可以用IC表示，用XCIX表示。

加线乘千：在一个罗马数字的上方加上一条横线或者在右下方写M，表示将这个数字乘以1000，即是原数的1000倍。
同理，如果上方有两条横线，即是原数的1000000倍。

单位限制：同样单位只能出现3次，如40不能表示为XXXX，而要表示为XL。
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mdict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ret = mdict[s[-1]]
        for i in range(0, len(s) - 1):
            if mdict[s[i]] < mdict[s[i + 1]]:
                ret -= mdict[s[i]]
            else:
                ret += mdict[s[i]]
        return ret


ss = Solution()
str1 = input()
print(ss.romanToInt(str1))