import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = res = ListNode()
        
        heap = [(value.val, idx) for idx, value in enumerate(lists) if value is not None]
        heapq.heapify(heap)

        while len(heap) != 0:
            cur_value, list_idx = heapq.heappop(heap)

            # add in merged list
            res.next = ListNode(cur_value)
            res = res.next

            # update of indexes
            lists[list_idx] = lists[list_idx].next
            if lists[list_idx] is None:
                continue

            # update the heap
            heapq.heappush(heap, (lists[list_idx].val, list_idx))
        
        return head.next


def test(fun, lists, res):
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
    
    lk_lists = []
    for i in lists:
        lk_lists.append(_gen_lk_list(i))
    
    sol = fun(lk_lists)
    degen_sol = _degen_lk_list(sol)
    
    if res == degen_sol:
        print("OK")
    else:
        print(_degen_lk_list(sol))
        print(res)
        print()

def main():
    s = Solution()
    
    test(
        s.mergeKLists,
        [[1,4,5],[1,3,4],[2,6]],
        [1,1,2,3,4,4,5,6]
    )
    test(
        s.mergeKLists,
        [],
        []
    )
    test(
        s.mergeKLists,
        [[]],
        []
    )

    
    return 0

if __name__ == '__main__':
    main()
