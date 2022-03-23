from Estruturas import TreeNode, print_tree, create_tree
from typing import List, Optional


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    stack = [root]
    resp = []
    while stack:
        atual = stack.pop()
        if atual is None:
            continue
        resp.append(atual.val)
        stack.extend([atual.right, atual.left])

    return resp


def main():
    a = [1, 2, None, 4, 5, 6, 7, 8]
    b = create_tree(a)
    print_tree(b)
    print(preorderTraversal(b))


if __name__ == '__main__':
    main()
