# Author: Jin


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def add(num1, num2):
            num1, num2 = num1[::-1], num2[::-1]
            carry, temp = 0, ''
            for i in range(min(len(num1), len(num2))):
                temp += str((int(num1[i]) + int(num2[i]) + carry) % 10)
                carry = (int(num1[i]) + int(num2[i]) + carry) // 10
            if len(num2) > len(num1):
                for i in range(len(num1), len(num2)):
                    temp += str((int(num2[i]) + carry) % 10)
                    carry = (int(num2[i]) + carry) // 10
            elif len(num2) < len(num1):
                for i in range(len(num2), len(num1)):
                    temp += str((int(num1[i]) + carry) % 10)
                    carry = (int(num1[i]) + carry) // 10
            if carry != 0:
                temp += str(carry)
            return temp[::-1]
        res = '0'
        if len(num1) > len(num2):
            for i in range(len(num2)):
                temp = num1 + '0' * i
                for j in range(int(num2[len(num2) - i - 1])):
                    res = add(res, temp)
        else:
            for i in range(len(num1)):
                temp = num2 + '0' * i
                for j in range(int(num1[len(num1) - i - 1])):
                    res = add(res, temp)
        return res

s = Solution()
n1 = '98'
n2 = '9'
print(s.multiply(n1, n2))