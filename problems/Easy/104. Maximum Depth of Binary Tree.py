from typing import Optional
from Estruturas import TreeNode, create_tree, print_tree


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))




def main():
    a = [3, 9, 20, None, None, 15, 7]
    h = create_tree(a)
    print_tree(h)
    print(maxDepth(h))


if __name__ == '__main__':
    main()
