from typing import Optional
from Structs.List import ListNode, create_linked_list, print_linked_list


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    cur = node_grupo = head
    p = 0
    while cur:
        print(cur.val, node_grupo.val)
        if p == 0:
            node_grupo = cur
        elif p == k:
            p = 0
            node_grupo.next = cur
            cur = cur.next
        cur = cur.next
        p += 1


def main():
    a = [1, 2, 3, 4, 5]
    b = 2
    h = create_linked_list(a)
    print_linked_list(h)
    h2 = reverseKGroup(h, b)
    print_linked_list(h2, debug=True)
    # h2 = reverse_lk_list_k(h, 4)


if __name__ == '__main__':
    main()

"""
n = 1
1 -> 2 -> 3 -> 4 -> 5 -> 6

n = 1
1 <- 2    3 -> 4 -> 5 -> 6

n = 1
1 <- 2 <- 3  4 -> 5 -> 6

n = 4
3 -> 2 -> 1 -> 4 -> 5 -> 6
"""