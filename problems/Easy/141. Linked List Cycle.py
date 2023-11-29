from typing import Optional

class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


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
	pass


if __name__ == '__main__':
    main()
