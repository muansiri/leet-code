# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        tmp = head
        while tmp:
            if tmp.next and tmp.next.val == val:
                p = tmp.next
                while p and p.val == val:
                    p = p.next
                tmp.next = p
            tmp = tmp.next
        return head
