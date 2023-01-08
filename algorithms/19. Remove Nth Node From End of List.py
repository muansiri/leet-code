# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        s, e = head, head
        for _ in range(n):
            e = e.next
        if not e:
            return head.next
        while (e.next):
            s, e = s.next, e.next
        s.next = s.next.next

        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """