from typing import Optional, List


class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


class TreeNode:
    def __init__(self, val, left=None, rihgt=None):
        self.val = val
        self.left = left
        self.right = rihgt

    def __str__(self):
        return str(self.val)


def create_linked_list(seq: list):
    """
    Create the linked list from a normal list
    :param seq: Sequence to transform in linked list
    :return: Head of list or None
    """
    if len(seq) == 0:
        return None
    head = ListNode(seq[0])
    current = head
    for i in seq[1:]:
        current.next = ListNode(i)
        current = current.next

    return head


def create_tree(seq):
    # seq_aux = [*map(lambda x:TreeNode if x is not None else None, seq)]
    # [1, null, 2]
    if len(seq) == 0:
        return None
    seq_aux = [*map(TreeNode, seq)]
    head = seq_aux.pop(0)
    queue = [head]
    while queue:
        atual = queue.pop(0)
        if atual is None:
            continue
        if seq_aux:
            temp = seq_aux.pop(0)
            atual.left = temp if temp.val is not None else None
            queue.append(atual.left)
        if seq_aux:
            temp = seq_aux.pop(0)
            atual.right = temp if temp.val is not None else None
            queue.append(atual.right)
    return head


def print_linked_list(lk_lst: ListNode, *, sep: str = ' -> '):
    temp = []
    cur = lk_lst
    while cur is not None:
        temp.append(cur.val)
        cur = cur.next
    print(sep.join(map(str, temp)))


def print_tree(node, prefix="", isLeft=True):
    """From leetCode"""
    if not node:
        print("Empty Tree")
        return

    if node.right:
        print_tree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        print_tree(node.left, prefix + ("    " if isLeft else "│   "), True)


def find_tree_node(h: TreeNode, val):
    stack = [h]
    while stack:
        cur = stack.pop()
        if cur is None:
            continue
        if cur.val == val:
            return cur

        stack.append(cur.left)
        stack.append(cur.right)
    return None


def main():
    # tests
    temp = create_tree([1, 2, 3])
    a = find_tree_node(temp, 1)
    print(a, temp)


if __name__ == '__main__':
    main()
