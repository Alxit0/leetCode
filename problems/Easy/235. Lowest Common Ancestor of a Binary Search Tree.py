from Structs.Binary_Tree import TreeNode, create_tree, print_tree, find_tree_node
from typing import Optional


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    while cur:
        if cur.val < p.val and cur.val < q.val:
            cur = cur.right
        elif cur.val > p.val and cur.val > q.val:
            cur = cur.left
        else:
            return cur


def main():
    a = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    b = 2
    c = 8
    h = create_tree(a)
    print_tree(h)
    print(lowestCommonAncestor(h, find_tree_node(h, b), find_tree_node(h, c)))


if __name__ == '__main__':
    main()
