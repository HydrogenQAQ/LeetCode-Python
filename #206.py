_author_ = 'Jin'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return head
        # ans = []
        # while head:
        #     ans.append(head)
        #     head = head.next
        # for i in range(len(ans) - 1, 0, -1):
        #     ans[i].next = ans[i - 1]
        # ans[0].next = None
        # return ans[-1]
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre


s = Solution()
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
head.next = node1
node1.next = node2
node2.next = node3
head = s.reverseList(head)
while head:
    print(head.val)
    head = head.next