import re
from typing import Optional, List
from Estruturas import TreeNode, print_tree, create_tree


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    stack = [root]
    resp = []
    while stack:
        node = stack.pop()
        if node is not None:
            resp.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return resp[::-1]


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    h = create_tree(a)
    print_tree(h)
    print(postorderTraversal(h))


if __name__ == '__main__':
    main()
