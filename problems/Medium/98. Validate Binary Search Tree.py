from typing import Optional
from Estruturas import TreeNode, create_tree, print_tree


def isValidBST(root: Optional[TreeNode], ini=-float('inf'), fin=float('inf')) -> bool:
    if root is None:
        return True
    if not (ini < root.val < fin):
        return False

    left = isValidBST(root.left, ini, min(fin, root.val))
    right = isValidBST(root.right, max(ini, root.val), fin)

    if not (right and left):
        return False

    if root.left is None:
        if root.right is None:
            return True
        elif root.right:
            return root.right.val > root.val
    elif root.right is None:
        return root.left.val < root.val
    else:
        return root.left.val < root.val < root.right.val


def main():
    a = [2,1,3]
    h = create_tree(a)
    print_tree(h)
    print(isValidBST(h))


if __name__ == '__main__':
    main()
