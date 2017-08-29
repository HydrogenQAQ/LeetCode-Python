# Author: Jin


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        copy = dummy
        while copy.next and copy.next.next:
            p = copy.next
            q = p.next
            copy.next = q
            p.next = q.next
            q.next = p
            copy = p
        return dummy.next

s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node1 = s.swapPairs(node1)
while node1:
    print(node1.val)
    node1 = node1.next