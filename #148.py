_author_ = 'Jin'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = []
        copy, copy2 = head, head
        while copy:
            ans.append(copy.val)
            copy = copy.next
        ans.sort()
        i = 0
        while copy2:
            copy2.val = ans[i]
            i += 1
            copy2 = copy2.next
        return head