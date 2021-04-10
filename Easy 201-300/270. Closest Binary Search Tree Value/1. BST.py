"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        res = root.val
        while root:
            res = min(res, root.val, key = lambda x: abs(target - x))
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return res