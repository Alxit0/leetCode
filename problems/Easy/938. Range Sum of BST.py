from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None: return 0
        stack = [root]
        s = root.val * (low <= root.val <= high)
        return s + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)