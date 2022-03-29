from typing import Optional
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if root1 is None:
        return root2
    if root2 is None:
        return root1

    root = TreeNode(root1.val + root2.val)
    root.left = mergeTrees(root1.left, root2.left)
    root.right = mergeTrees(root1.right, root2.right)

    return root


def main():
    a = [1, 3, 2, 5]
    b = [2, 1, 3, None, 4, None, 7]
    h1 = create_tree(a)
    h2 = create_tree(b)
    h3 = mergeTrees(h1, h2)
    print_tree(h3)


if __name__ == '__main__':
    main()
