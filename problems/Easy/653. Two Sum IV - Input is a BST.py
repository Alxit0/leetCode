from Estruturas import TreeNode, print_tree, create_tree
from typing import Optional, List


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    stack = [root]
    nums = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.val in nums:
            return True
        nums.add(k - node.val)
        stack.extend([node.left, node.right])
    return False


def main():
    a = [5,3,6,2,4,None,7]
    h = create_tree(a)
    print_tree(h)
    print(findTarget(h, 9))


if __name__ == '__main__':
    main()
