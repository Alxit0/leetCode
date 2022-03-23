from Estruturas import TreeNode, create_tree, print_tree
from typing import Optional


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root
    temp = invertTree(root.left)
    root.left = invertTree(root.right)
    root.right = temp

    return root


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    h = create_tree(a)
    print_tree(h)
    print_tree(invertTree(h))


if __name__ == '__main__':
    main()
