from typing import Optional
from Estruturas import ListNode, create_linked_list, print_linked_list


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    ant = None
    eu = head

    while eu is not None:
        temp = eu.next
        eu.next = ant
        ant = eu
        eu = temp
    return ant


def main():
    a = [1, 2, 3, 4, 5]
    lk = create_linked_list(a)
    print_linked_list(lk)
    resp = reverseList(lk)
    print_linked_list(resp)


if __name__ == '__main__':
    main()
