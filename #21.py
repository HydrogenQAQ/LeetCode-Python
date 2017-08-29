# Author: Jin

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = l3 = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next
        l3.next = l1 or l2
        return root.next

l1 = ListNode(1)
l2 = ListNode(2)
s = Solution()
ln = s.mergeTwoLists(l1, l2)
while ln:
    print(ln.val)
    ln = ln.next

