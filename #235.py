# -*- coding: utf-8 -*-

"""
@author: Jinqf
@file: #235
@time: 2017/8/30 12:32
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val <= root.val <= q.val:
            return root