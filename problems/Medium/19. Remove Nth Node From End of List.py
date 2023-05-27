# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next: ListNode = next

def create_linked_list(seq: list):
    """
    Create the linked list from a normal list
    :param seq: Sequence to transform in linked list
    :return: Head of list or None
    """
    if len(seq) == 0:
        return None
    head = ListNode(seq[0])
    current = head
    for i in seq[1:]:
        current.next = ListNode(i)
        current = current.next

    return head

def print_linked_list(lk_lst: ListNode, *, sep: str = ' -> '):
    temp = []
    cur = lk_lst
    while cur is not None:
        temp.append(cur.val)
        cur = cur.next
    print(sep.join(map(str, temp)))


from typing import Optional

class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		
		cur = head
		for _ in range(n):
			cur = cur.next

		if cur is None:
			return head.next

		to_del = head
		while cur.next is not None:
			cur = cur.next
			to_del = to_del.next
		

		to_del.next = to_del.next.next

		return head

	
	
	
if __name__ == "__main__":
	nums = [1, 2, 3, 4, 5, 6]
	n = 6

	head = create_linked_list(nums)
	print_linked_list(head)
	print_linked_list(Solution().removeNthFromEnd(head, n))

	# for i in range(len(nums)):
	# 	head = create_linked_list(nums)
	# 	print_linked_list(Solution().removeNthFromEnd(head, i+1))
