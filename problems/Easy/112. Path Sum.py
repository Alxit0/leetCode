from typing import Optional
from Estruturas import TreeNode, create_tree, print_tree


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False
    if root.left is None and root.right is None:
        return targetSum - root.val == 0

    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


def main():
    a = [1, None, 3, 2]
    h = create_tree(a)
    print_tree(h)
    print(hasPathSum(h, 6))


if __name__ == '__main__':
    main()
