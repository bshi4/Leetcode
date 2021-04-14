# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        def helper(root, flag):
            if not root:
                return 0
            if not root.left and not root.right and flag:
                return root.val
            
            return helper(root.left, True) + helper(root.right, False)
        
        return helper(root, False)