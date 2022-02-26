from typing import Optional


class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


def create_linked_list(seq: Optional[str, list]) -> Optional[ListNode, None]:
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


def print_linked_list(lk_lst: ListNode, *, sep: str = ' -> '):
    temp = []
    cur = lk_lst
    while cur is not None:
        temp.append(cur.val)
        cur = cur.next
    print(sep.join(map(str, temp)))


def main():
    # tests
    temp = create_linked_list([1, 2, 3])
    print(temp.val)
    print(temp.next.val)
    print(temp.next.next.val)


if __name__ == '__main__':
    main()
