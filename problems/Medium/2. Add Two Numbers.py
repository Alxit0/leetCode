# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2 -- 4 -- 3
# 5 -- 6 -- 4
# 7 -- 0 -- 8

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pt1 = l1
        pt2 = l2
        resp = []
        sobra = 0
        while pt1 is not None or pt2 is not None:
            if pt1 is not None:
                a = pt1.val
                pt1 = pt1.next
            else:
                a = 0

            if pt2 is not None:
                b = pt2.val
                pt2 = pt2.next
            else:
                b = 0

            val = a + b + sobra
            sobra = val // 10
            resp += val % 10,
        if sobra: resp += sobra,
        temp = ListNode(resp[-1])
        for i in resp[:-1][::-1]:
            temp = ListNode(i, temp)
        return temp


if __name__ == '__main__':
    a = Solution()
