class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex


def create_linked_list(seq):
    if len(seq) == 0:
        return None
    head = ListNode(seq[0])
    cur = head
    for i in seq[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    return head


def main():
    temp = create_linked_list([1, 2, 3])
    print(temp.val)
    print(temp.next.val)
    print(temp.next.next.val)


if __name__ == '__main__':
    main()
