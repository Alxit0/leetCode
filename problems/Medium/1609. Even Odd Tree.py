from typing import Optional
from Estruturas import TreeNode, create_tree


def isEvenOddTree(root: Optional[TreeNode]) -> bool:
    queue = [root]
    lvl = 0
    while queue:
        temp = list(map(lambda x: x.val, queue))
        if len(temp) != len(set(temp)):
            return False

        if any(i % 2 == lvl % 2 for i in temp) or temp != sorted(temp)[::(-1)**lvl]:
            return False

        temp = []
        for i in queue:
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        queue = temp[:]
        lvl += 1

    return True


def main():
    # a = [1,10,4,3,None,7,9,12,8,6,None,None,2]
    a = [5,4,2,3,3,7]
    h = create_tree(a)
    print(isEvenOddTree(h))


if __name__ == '__main__':
    main()