# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(val=0, next=head)
        current = ans
        while current:
            if current.next and current.next.val == val:
                next = current.next
                while next and next.val == val:
                    next = next.next
                current.next = next
            current = current.next
        return ans.next
