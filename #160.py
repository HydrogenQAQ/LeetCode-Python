_author_ = 'Jin'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        # ans1, ans2 = [], []
        # while headA:
        #     ans1.append(headA)
        #     headA = headA.next
        # while headB:
        #     ans2.append(headB)
        #     headB = headB.next
        # i = -1
        # if ans2[i] != ans1[i]:
        #     return None
        # while ans1[i] == ans2[i]:
        #     i -= 1
        #     if abs(i) > len(ans1) or abs(i) > len(ans2):
        #         break
        # return ans1[i + 1]
        l1, l2 = 0, 0
        copy1, copy2 = headA, headB
        while headA:
            l1 += 1
            headA = headA.next
        while headB:
            l2 += 1
            headB = headB.next
        diff = abs(l1 - l2)
        if l1 > l2:
            while diff:
                copy1 = copy1.next
                diff -= 1
        else:
            while diff:
                copy2 = copy2.next
                diff -= 1
        while copy1 and copy2:
            if copy1 == copy2:
                return copy1
            copy1 = copy1.next
            copy2 = copy2.next
        return None


s = Solution()
headA = ListNode(1)
headB = ListNode(2)
node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(6)
node5 = ListNode(7)
headA.next = node1
headB.next = node2
node2.next = node3
node3.next = node4
node1.next = node4
node4.next = node5
print(s.getIntersectionNode(headA, headB).val)



