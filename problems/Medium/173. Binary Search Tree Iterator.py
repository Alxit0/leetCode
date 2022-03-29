from typing import Optional
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def helper(root: TreeNode):
    if root is None:
        return []

    return helper(root.left) + [root.val] + helper(root.right)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.lista = helper(root)
        self.idx: int = -1

    def next(self) -> int:
        self.idx += 1
        return self.lista[self.idx]

    def hasNext(self) -> bool:
        return self.idx+1 < len(self.lista)


def main():
    a = [7, 3, 15, None, None, 9, 20]
    h = create_tree(a)
    print_tree(h)
    ordens = ["BSTIterator", "next", "next", "hasNext", "next",
              "hasNext", "next", "hasNext", "next", "hasNext"]
    obj = BSTIterator(h)
    for i in ordens[1:]:
        exec(f"print(obj.{i}())")


if __name__ == '__main__':
    main()
