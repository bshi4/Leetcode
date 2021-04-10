# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res
        
        def dfs(root, res, s):
            if not root:
                return
            if not root.left and not root.right:
                s += str(root.val)
                res.append(s)
            s += str(root.val) + '->'
            
            dfs(root.left, res, s)
            dfs(root.right, res, s)
        
        dfs(root, res, '')
        return res