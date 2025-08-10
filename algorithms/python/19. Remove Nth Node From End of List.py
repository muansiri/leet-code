# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count_node = 1
        tail = head
        while tail.next:
            tail = tail.next
            count_node += 1

        if n == count_node:
            return head.next

        tmp = head
        for i in range(1, count_node - n):
            tmp = tmp.next
        tmp.next = tmp.next.next if tmp.next.next else None
        return head
