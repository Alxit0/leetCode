from typing import Optional

class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        if list2 is None:
            return None
        else:
            return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        return ListNode(list1.val, mergeTwoLists(list1.next, list2))
    return ListNode(list2.val, mergeTwoLists(list1, list2.next))


def main():
    pass

if __name__ == '__main__':
    main()

