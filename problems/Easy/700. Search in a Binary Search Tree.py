from typing import Optional
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        # print(node.val)
        if node is None:
            continue

        if node.val == val:
            return node

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return None


def main():
    a = [4, 2, 7, 1, 3]
    h = create_tree(a)
    print_tree(h)
    print_tree(searchBST(h, 9))


if __name__ == '__main__':
    main()
