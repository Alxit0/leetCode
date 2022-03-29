from typing import List, Optional
from Structs.Binary_Tree import TreeNode, print_tree


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) == 0:
        return

    root = TreeNode(preorder[0])

    temp = inorder.index(preorder[0])
    # print(inorder[:temp], preorder[1:temp+1])
    # print(inorder[temp+1:], preorder[temp+1:])

    root.left = buildTree(preorder[1:temp+1], inorder[:temp])
    root.right = buildTree(preorder[temp+1:], inorder[temp+1:])

    return root


def main():
    a = [3, 9, 20, 15, 7]
    b = [9, 3, 15, 20, 7]
    h = buildTree(a, b)
    print_tree(h)


if __name__ == '__main__':
    main()
