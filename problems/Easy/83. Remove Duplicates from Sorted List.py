from typing import Optional
from Estruturas import ListNode, create_linked_list, print_linked_list


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
    a = []
    lk = create_linked_list(a)
    resp = deleteDuplicates(lk)
    print_linked_list(resp)


if __name__ == '__main__':
    main()
