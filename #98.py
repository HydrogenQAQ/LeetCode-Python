# Author: Jin


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dp(root):
            if root.left:
                dp(root.left)
            res.append(root.val)
            if root.right:
                dp(root.right)
        res = []
        dp(root)
        if not root:
            return True
        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False
        return True

s = Solution()
n1 = TreeNode(None)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n1.left = n2
# n1.right = n3
print(s.isValidBST(n1))