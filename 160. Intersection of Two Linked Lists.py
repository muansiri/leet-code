# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA:
            headA.passed = True
            headA = headA.next

        while headB:
            if hasattr(headB, 'passed'):
                return headB
            headB = headB.next
        return None
