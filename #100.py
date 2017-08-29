# Author: Jin


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        isA = True

        def isSame(p, q, isA):
            if p is not None and q is not None:
                if p.val != q.val:
                    isA = False
                isSame(p.left, q.left, isA)
                isSame(p.right, q.right, isA)
            elif p is None and q is None:
                isA = True
            else:
                isA = False
            return isA
        if isSame(p, q, isA) is False:
            return False
        else:
            return True

s = Solution()
n1 = TreeNode(0)
n2 = TreeNode(1)
n3 = TreeNode(2)
n1.left = n2
n1.right = n3
n4 = TreeNode(0)
n5 = TreeNode(1)
n6 = TreeNode(2)
n4.left = n5
n5.right = n6
print(s.isSameTree(n1, n4))