from typing import Optional
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def sumNumbers(root: Optional[TreeNode]) -> int:
    resp = 0

    stack = [(root, 0)]
    while stack:
        cur, valor_atual = stack.pop()
        valor_atual = valor_atual*10 + cur.val

        # print(valor_atual)
        if cur.left is None and cur.right is None:
            resp += valor_atual

        if cur.left:
            stack.append((cur.left, valor_atual))
        if cur.right:
            stack.append((cur.right, valor_atual))

    return resp


def main():
    a = [1, 5, 1, None, None, None, 6]
    h = create_tree(a)
    print_tree(h)
    print(sumNumbers(h))


if __name__ == '__main__':
    main()
