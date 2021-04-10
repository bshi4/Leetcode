# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        q = [root]
        res = 0
        while q:
            tq = []
            for n in q:
                if n.left:
                    tq.append(n.left)
                if n.right:
                    tq.append(n.right)
            q = tq
            res += 1
        return res

            