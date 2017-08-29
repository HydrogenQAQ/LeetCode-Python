# Author: Jin
from LeetCode import LinkedList


class Solution(object):
    def isPalindrome(self, head):
        """
        判断是否为回文列表
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        list_node = []
        while head:
            list_node.append(head.val)
            head = head.next
        if list_node == list_node[::-1]:
            return True
        else:
            return False

l = LinkedList.List()
l.insert(1)
print(type(l))
s = Solution()
# print(s.isPalindrome(l))