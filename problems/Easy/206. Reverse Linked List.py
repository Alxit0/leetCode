from typing import Optional

class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


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
    pass

if __name__ == '__main__':
    main()
