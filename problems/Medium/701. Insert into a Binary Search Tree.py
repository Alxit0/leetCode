from typing import Optional
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    cur = root
    while cur:
        temp = cur.val
        if temp < val:
            if cur.right:
                cur = cur.right
            else:
                cur.right = TreeNode(val)
                return root
        else:
            if cur.left:
                cur = cur.left
            else:
                cur.left = TreeNode(val)
                return root
    else:
        return TreeNode(val)


def main():
    a = []
    h = create_tree(a)
    print_tree(h)
    print_tree(insertIntoBST(h, 5))


if __name__ == '__main__':
    main()
