from typing import Optional
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def isSyme(lf, rt):
        if not lf and not rt:
            return True
        if lf and rt and lf.val == rt.val:
            return isSyme(lf.left, rt.right) and isSyme(lf.right, rt.left)
        return False

    return isSyme(root.left, root.right)


def main():
    a = [1, 2, 2, 3, 4, 4, 3]
    h = create_tree(a)
    print_tree(h)
    print(isSymmetric(h))


if __name__ == '__main__':
    main()
