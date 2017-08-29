# Author: Jin


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        ans = []

        def preOrderTravel(root):
            if not root:
                return
            ans.append(root)
            preOrderTravel(root.left)
            preOrderTravel(root.right)
        preOrderTravel(root)
        copy = root
        for i in range(1, len(ans)):
            copy.left = None
            copy.right = ans[i]
            copy = ans[i]

s = Solution()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
root.left = node1
root.right = node4
node1.left = node2
node1.right = node3
node4.right = node5
s.flatten(root)
