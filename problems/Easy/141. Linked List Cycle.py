from typing import Optional
from Estruturas import ListNode, create_linked_list


def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    temp = set()
    cur = head
    while cur.next is not None:
        if cur in temp:
            return True
        temp.add(cur)
        cur = cur.next
    return False


def main():
    a = [1, 2, 3, 4, 5, 6, 7]
    b = -1

    array = create_linked_list(a)
    cur = array
    p = 0
    target = None
    while b != -1 and cur.next is not None:
        if p == b:
            target = cur
        cur = cur.next
        p += 1
    else:
        if b!=-1:
            cur.next = target

    print(hasCycle(array))


if __name__ == '__main__':
    main()
