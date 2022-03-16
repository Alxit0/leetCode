from Estruturas import create_linked_list, ListNode, print_linked_list
from typing import Optional


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.val == head.next.val:
        while head.val == head.next.val:
            head = head.next
        head = head.next
    cur = head
    while cur.next:
        temp = cur.next
        # print(cur.val)
        while temp.next and cur.next.val == temp.next.val:
            temp = temp.next
        cur.next = temp.next
        cur = cur.next

    return head


def main():
    a = [1, 1, 2, 3, 3, 4, 5, 6]
    h = create_linked_list(a)
    print_linked_list(h)
    h2 = deleteDuplicates(h)
    print_linked_list(h2)


if __name__ == '__main__':
    main()
