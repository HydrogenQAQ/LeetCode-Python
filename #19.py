# Author: Jin


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1
        copy1, copy2 = head, head
        while copy1.next:
            copy1 = copy1.next
            length += 1
        for i in range(length - n - 1):
            copy2 = copy2.next
        if length == n:
            head = head.next
            return head
        if copy2.next.next is None:
            copy2.next = None
        else:
            copy2.next = copy2.next.next
        return head

s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
link = s.removeNthFromEnd(node1, 3)
while link:
    print(link.val)
    link = link.next
