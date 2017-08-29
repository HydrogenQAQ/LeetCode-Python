# Author: Jin


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def isMirror(root1, root2):
        #     if not root1 and not root2:
        #         return True
        #     if not root1 or not root2:
        #         return False
        #     return (root1.val == root2.val) and isMirror(root1.left, root2.right)
        # and isMirror(root1.right, root2.left)
        # return isMirror(root, root)
        if not root:
            return True
        ans = []

        def inOrderTravel(root):
            if root.left:
                inOrderTravel(root.left)
            ans.append(root.val)
            if root.right:
                inOrderTravel(root.right)

        def preOrderTravel(root):
            ans.append(root.val)
            if root.left:
                preOrderTravel(root.left)
            if root.right:
                preOrderTravel(root.right)

        def invert(root):
            temp = root.left
            root.left = root.right
            root.right = temp
            if root.left:
                invert(root.left)
            if root.right:
                invert(root.right)
        inOrderTravel(root)
        preOrderTravel(root)
        invert(root)
        inOrderTravel(root)
        preOrderTravel(root)
        # print(ans[:len(ans) // 2], [ans[len(ans) // 2:]])
        if ans[:len(ans) // 2] == ans[len(ans) // 2:]:
            return True
        else:
            return False


s = Solution()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(3)
node4 = TreeNode(2)
root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
print(s.isSymmetric(root))
