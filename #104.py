# Author: Jin


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0
            else:
                a = depth(root.left)
                b = depth(root.right)
                return a + 1 if a > b else b + 1
        res = depth(root)
        return res

s = Solution()
root = TreeNode(1)
print(s.maxDepth(root))