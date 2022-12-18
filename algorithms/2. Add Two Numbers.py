# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current_node = result
        current_val = 0
        while (l1 or l2 or current_val):
            if l1:
                current_val += l1.val
                l1 = l1.next
            if l2:
                current_val += l2.val
                l2 = l2.next

            current_node.next = ListNode(current_val % 10)
            current_node = current_node.next
            current_val = current_val // 10
        return result.next