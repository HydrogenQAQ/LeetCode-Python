# Author: Jin


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        判断一个链表更加常用的方法是设置两个指针（一个快一个慢）如果最终两个指针能相遇
        那么该链表必定有环
        """
        cnt = 0
        while head and cnt < 1000:
            head = head.next
            cnt += 1
        if cnt == 1000:
            return True
        else:
            return False
