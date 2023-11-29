from typing import Optional

class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head is not None and head.val == val:
        head = head.next

    if head is None:
        return None

    cur = head
    while cur.next is not None:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def main():
    pass


if __name__ == '__main__':
    main()
