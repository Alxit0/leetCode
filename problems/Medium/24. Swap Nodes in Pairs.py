from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev = save = ListNode(None, head)
        cur = head

        while cur and cur.next:
            sec: ListNode = cur.next

            # make the switch
            prev.next = sec
            cur.next, sec.next = sec.next, cur
            
            # update pointers
            prev, cur = cur, cur.next
        
        return save.next




def test(fun, case, res):
    def _gen_lk_list(nums):
        res = head = ListNode()
        for i in nums:
            res.next = ListNode(i)
            res = res.next
        
        return head.next
    
    def _degen_lk_list(lk_list):
        res = []
        
        cur = lk_list
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        
        return res
    
    lk_case = _gen_lk_list(case)
    sol = _degen_lk_list(fun(lk_case))
    
    if sol == res:
        print("OK")
    else:
        print(sol)
        print(res)
        print()

def main():
    s = Solution()

    test(
        s.swapPairs,
        [1,2,3,4],
        [2,1,4,3]
    )
    test(
        s.swapPairs,
        [],
        []
    )
    test(
        s.swapPairs,
        [1],
        [1]
    )

if __name__ == '__main__':
    main()
