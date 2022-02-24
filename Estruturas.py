class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


def create_linked_list(seq):
    """
    Create the linked list from a normal list
    :return: the head of the list
    """
    if len(seq) == 0:
        return None
    head = ListNode(seq[0])
    current = head
    for i in seq[1:]:
        current.next = ListNode(i)
        current = current.next

    return head


def main():
    # tests
    temp = create_linked_list([1, 2, 3])
    print(temp.val)
    print(temp.next.val)
    print(temp.next.next.val)


if __name__ == '__main__':
    main()
