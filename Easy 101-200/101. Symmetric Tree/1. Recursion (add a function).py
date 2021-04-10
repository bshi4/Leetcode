# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        else:
            return self.isSymmetric2(root.left, root.right)
    
    def isSymmetric2(self, left, right):
        if not left and not right:
            return True
        elif not left or not right or left.val != right.val:
            return False
        else:
            return self.isSymmetric2(left.left, right.right) and self.isSymmetric2(left.right, right.left)
