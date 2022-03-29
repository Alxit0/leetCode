from typing import Optional, List
from Structs.Binary_Tree import TreeNode, create_tree


def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    resp = []
    queue = [root]
    while queue:
        resp.append([i.val for i in queue])
        temp = []
        for i in queue:
            if i.left:
                temp.append(i.left)

            if i.right:
                temp.append(i.right)
        queue = temp
    return resp[::-1]


def main():
    a = [3, 9, 20, None, None, 15, 7]
    h = create_tree(a)
    print(levelOrderBottom(h))


if __name__ == '__main__':
    main()
