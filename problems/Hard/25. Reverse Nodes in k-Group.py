"""
not done
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check lenght at least k
        cur = head
        for _ in range(k):
            if cur is None:
                return head
            
            cur = cur.next

        # reverse list k elements
        prev = None
        cur = head
        for _ in range(k):
            next_node = cur.next
            cur.next = prev
            
            prev = cur
            cur = next_node
        
        head.next = self.reverseKGroup(cur, k)
        
        return prev



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
    
    nums, k = case
    lk_nums = _gen_lk_list(nums)
    sol = _degen_lk_list(fun(lk_nums, k))
    
    if sol == res:
        print("OK")
    else:
        print(sol)
        print(res)
        print()

def main():
    s = Solution()

    test(
        s.reverseKGroup,
        ([1,2,3,4,5], 2),
        [2,1,4,3,5]
    )
    test(
        s.reverseKGroup,
        ([1,2,3,4,5], 3),
        [3,2,1,4,5]
    )
    test(
        s.reverseKGroup,
        ([1,2], 2),
        [2,1]
    )

if __name__ == '__main__':
    main()
