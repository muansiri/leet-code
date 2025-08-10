# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(next=head)
        p = h
        while p.next and p.next.next:
            first, second, after = p.next, p.next.next, p.next.next.next
            first.next = after
            second.next = first
            p.next = second
            p = first
        return h.next
