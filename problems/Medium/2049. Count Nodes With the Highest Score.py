from typing import List
from Estruturas import print_tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.tam = 1
        self.left: Node = left
        self.right: Node = right

    def __str__(self):
        return f"{self.tam}"


def generate_tree(seq):
    resp = list(map(Node, range(len(seq))))
    # print(*resp)

    for i, j in enumerate(seq[1:]):
        if resp[j].left is None:
            resp[j].left = resp[i+1]
        else:
            resp[j].right = resp[i+1]

    return resp


def get_tams(root:Node):
    if root is None:
        return 0

    root.tam = 1 + get_tams(root.left) + get_tams(root.right)

    return root.tam


def countHighestScoreNodes(parents: List[int]) -> int:
        h = generate_tree(parents)
        get_tams(h[0])

        highs = []
        for i in h:
            temp = 1
            if i.val != 0:
                temp = h[0].tam - i.tam

            if i.left:
                temp *= i.left.tam
            if i.right:
                temp *= i.right.tam
            highs.append(temp)
        return highs.count(max(highs))


def main():
    a = [-1, 2, 0, 2, 0]
    print(countHighestScoreNodes(a))


if __name__ == '__main__':
    main()
