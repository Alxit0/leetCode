from Estruturas import print_tree
from random import randint


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.gate = 0


class MaxHeap:
    def __init__(self, head=None):
        self.head: Node = head
        self.tam = 0

    def insert(self, val) -> None:
        if self.head is None:
            self.head = Node(val)
            self.tam = 2
            return

        cur = self.head
        path = bin(self.tam)[3:]
        for i in path:
            if cur.val < val:
                temp = cur.val
                cur.val = val
                val = temp

            if cur.left is None:
                cur.left = Node(val)
                break
            elif cur.right is None:
                cur.right = Node(val)
                break
            cur = cur.left if i == '0' else cur.right

        self.tam += 1

    def pop(self):
        if self.tam == 0:
            print('Heap vazia')
            return

        cur = self.head
        print(bin(self.tam)[2:])
        for i in bin(self.tam-1)[3:-1]:
            next_node: Node = cur.left if i == '0' else cur.right
            cur.val = next_node.val
            cur = next_node

        # print(cur.val)


def main():
    test = MaxHeap()
    a = [randint(0, 100) for _ in range(101)]
    for i in a:
        test.insert(i)
    print_tree(test.head)
    test.pop()
    print_tree(test.head)


if __name__ == '__main__':
    main()
