from typing import Optional
from Estruturas import ListNode, create_linked_list, print_linked_list


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
    a = [6, 6]
    b = 6
    lk = create_linked_list(a)

    resposta = removeElements(lk, b)
    print_linked_list(resposta)


if __name__ == '__main__':
    main()
