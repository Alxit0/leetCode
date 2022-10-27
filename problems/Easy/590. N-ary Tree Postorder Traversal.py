from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node, resp=None) -> List[int]:
        if root is None:
            return []
        if resp is None:
            resp = []
        
        for i in root.children:
            self.postorder(i, resp)
        resp.append(root.val)
        return resp