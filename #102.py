# Author: Jin


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, ans = [], []
        q = [root]
        end = TreeNode('#')
        q.append(end)
        while True:
            temp = q.pop(0)
            if len(q) != 0 and temp.val == '#':
                q.append(end)
                res.append(ans)
                ans = []
            elif temp.val == '#' and len(q) == 0:
                res.append(ans)
                break
            else:
                ans.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return res
        # if not root:
        #     return []
        # import queue
        # res, ans = [], []
        # q = queue.Queue()
        # q.put(root)
        # end = TreeNode('#')
        # q.put(end)
        # while True:
        #     temp = q.get()
        #     if q.qsize() != 0 and temp.val == '#':
        #         q.put(end)
        #         res.append(ans)
        #         ans = []
        #     elif temp.val == '#' and q.qsize() == 0:
        #         res.append(ans)
        #         break
        #     else:
        #         ans.append(temp.val)
        #         if temp.left:
        #             q.put(temp.left)
        #         if temp.right:
        #             q.put(temp.right)
        # return res

s = Solution()
root = TreeNode(3)
node1 = TreeNode(11)
node2 = TreeNode(22)
root.right = node1
node1.left = node2
print(s.levelOrder(root))

