from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        fake = ListNode(-1, head)

        ant, cur = fake, head

        while cur and cur.next :
            if cur.val != cur.next.val:
                ant, cur = cur, cur.next
                continue

            while cur.next is not None and cur.val == cur.next.val:
                cur = cur.next
            
            ant.next = cur.next
            cur = cur.next
        
        return fake.next


def test_case(s:Solution, vals, res):
    def _create_list():
        if len(vals) == 0:
            return []
        
        head = cur = ListNode(vals[0])

        for i in vals[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        
        return head

    def _get_list(head: ListNode):
        r = []
        
        while head:
            r.append(head.val)
            head = head.next
        
        return r

    lk_list = _create_list()

    ans = s.deleteDuplicates(lk_list)
    
    print(vals, _get_list(ans), res)

def main():
    s = Solution()

    test_case(s, [1, 1], [])
    test_case(s, [1, 1, 1, 2, 3], [2, 3])

if __name__ == '__main__':
    main()
