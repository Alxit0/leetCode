from typing import Optional

class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    cur = head
    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def main():
    pass

if __name__ == '__main__':
    main()
