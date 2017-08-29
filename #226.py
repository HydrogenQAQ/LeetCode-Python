# -*- coding: utf-8 -*-

"""
@author: Jinqf
@file: #226
@time: 2017/8/27 14:29
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def preOrder(root):
            temp = root.left
            root.left = root.right
            root.right = temp
            if root.left:
                preOrder(root.left)
            if root.right:
                preOrder(root.right)
        if not root:
            return root
        preOrder(root)
        return root

root1 = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(6)
node6 = TreeNode(9)
root1.left = node1
root1.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
s = Solution()
# s.invertTree(root1)
root2 = TreeNode(1)
node9 = TreeNode(2)
root2.left = node9
s.invertTree(root2)