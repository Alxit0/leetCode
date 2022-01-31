from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root) -> List[float]:
        util = self._averageOfLevels(root, 0, {})
        return [i / j for i, j in util.values()]

    def _averageOfLevels(self, root, lvl, s):
        if lvl not in s: s[lvl] = [0, 0]
        s[lvl][0] += root.val
        s[lvl][1] += 1

        if root.left is not None:
            self._averageOfLevels(root.left, lvl + 1, s)

        if root.right is not None:
            self._averageOfLevels(root.right, lvl + 1, s)

        return s