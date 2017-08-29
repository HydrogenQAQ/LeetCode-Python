# Author: Jin


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        c = ''
        l1, l2 = min(len(a), len(b)), max(len(a), len(b))
        for i in range(-1, -1 - l1, -1):
            temp = (int(a[i]) + int(b[i]) + carry) % 2
            carry = int((int(a[i]) + int(b[i]) + carry) / 2)
            c += str(temp)
            i -= 1
        if len(a) > len(b):
            for i in range(-1 - l1, -l2 - 1, -1):
                temp = (int(a[i]) + carry) % 2
                carry = int((int(a[i]) + carry) / 2)
                c += str(temp)
                i -= 1
        else:
            for i in range(-1 - l1, -l2 - 1, -1):
                temp = (int(b[i]) + carry) % 2
                carry = int((int(b[i]) + carry) / 2)
                c += str(temp)
                i -= 1
        if carry == 1:
            c += str(carry)
        return c[::-1]

s = Solution()
a = input()
b = input()
print(s.addBinary(a, b))