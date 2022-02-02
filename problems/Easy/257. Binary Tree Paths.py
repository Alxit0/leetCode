from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self._binaryTreePaths(root, [], [])

    def _binaryTreePaths(self, root, current, resp):
        if root is None:
            return

        if root.left is None and root.right is None:
            resp += '->'.join(map(str, current + [root.val])),
            return resp

        self._binaryTreePaths(root.left, current + [root.val], resp)
        self._binaryTreePaths(root.right, current + [root.val], resp)

        return resp
