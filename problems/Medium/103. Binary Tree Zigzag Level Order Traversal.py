from typing import Optional, List
from Structs.Binary_Tree import *


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    resp = []
    pointer = 0
    queue = [root]
    while queue:
        temp = []
        temp2 = []
        for i in queue:
            if pointer % 2 == 0:
                temp2.append(i.val)
            else:
                temp2.insert(0, i.val)

            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        resp.append(temp2)
        queue = temp
        pointer += 1

    return resp


def main():
    a = [3, 9, 20, None, None, 15, 7]
    h = create_tree(a)
    print(zigzagLevelOrder(h))


if __name__ == '__main__':
    main()
