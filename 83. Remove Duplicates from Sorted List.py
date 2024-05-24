# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            next_item = current.next
            while next_item and next_item.val == current.val:
                next_item = next_item.next
            current.next = next_item
            current = current.next
        return head