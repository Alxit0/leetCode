class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

class Solution:...

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

    ans = s.qualquer_coisa(lk_list)
    
    print(vals, _get_list(ans), res)