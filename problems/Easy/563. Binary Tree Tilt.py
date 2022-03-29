from typing import Optional
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def findTilt(root: Optional[TreeNode]) -> int:
    resp = 0

    def node_sum(node: TreeNode):
        nonlocal resp
        if node is None:
            return 0

        temp_l = node_sum(node.left)
        temp_r = node_sum(node.right)
        resp += abs(temp_l - temp_r)

        return node.val + temp_l + temp_r

    node_sum(root)

    return resp


def main():
    a = [21, 7, 14, 1, 1, 2, 2, 3, 3]
    h = create_tree(a)
    print(findTilt(h))


if __name__ == '__main__':
    main()
