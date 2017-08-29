# Author: Jin


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 设置快慢指针
        quick = head
        slow = head
        if not head or not head.next or not head.next.next:
            return
        while True:
            if not quick.next or not quick.next.next:
                return None
            quick = quick.next.next
            slow = slow.next
            if quick.val == slow.val:
                break
        quick = head
        while quick != slow:
            quick = quick.next
            slow = slow.next
        return slow

s = Solution()
head = ListNode(1)
print(s.detectCycle(head))
