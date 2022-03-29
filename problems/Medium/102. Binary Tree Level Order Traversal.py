from Structs.Binary_Tree import TreeNode, create_tree, print_tree
from typing import Optional, List


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    resp = []
    queue = [root] if root else []
    while queue:
        temp = []
        md = 0
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node is None:
                continue
            temp.append(node.val)
            queue.extend([node.left, node.right])
            md += 2
        resp.append(temp)
    if resp:
        del resp[-1]
    return resp


def main():
    a = [1, 2, 3, 4, 5, 6]
    h = create_tree(a)
    print_tree(h)
    print(levelOrder(h))


if __name__ == '__main__':
    main()
