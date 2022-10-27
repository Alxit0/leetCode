"""
not finished
"""

from typing import List, Optional

def print_tree(node, prefix="", isLeft=True):
    """From leetCode"""
    if not node:
        print("Empty Tree")
        return

    if node.right:
        print_tree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node))

    if node.left:
        print_tree(node.left, prefix + ("    " if isLeft else "│   "), True)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def repr_helper(self):
        if self.left is None and self.right is None:
            return [self.val, self.left, self.right]
        return [self.val, *self.left.repr_helper(), *self.right.repr_helper()]

    def __repr__(self) -> str:
        # return str(self.repr_helper())
        return str(self.val)

"""
1: [[0]]
2: []
3: [[0,0,0]]
4: []
5: [[0,0,0,null,null,0,0],[0,0,0,0,0]]
"""

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}
        memo[1] = (TreeNode(), )
        memo[3] = (TreeNode(0, TreeNode(), TreeNode()),)
        self.allPossibleFBT_helper(n, memo)
        return list(memo[n])

    def allPossibleFBT_helper(self, n: int, memo: dict):
        temp = memo.get(n)
        if temp is not None:
            return temp
        
        self.allPossibleFBT_helper(n-2, memo)
        resp = []
        for i in memo[n-2]:
            resp.append(TreeNode(0, i, TreeNode()))
            resp.append(TreeNode(0, TreeNode(), i))
        
        for i in memo.get(n//2, []):
            resp.append(TreeNode(0, i, i))
        
        memo[n] = tuple(resp)

if __name__ == '__main__':
    s = Solution()
    a = s.allPossibleFBT(9)
    for i in a:
        print_tree(i)
        input("_______")
