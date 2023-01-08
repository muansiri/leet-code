# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        previos_node = None
        current_node = head
        is_first_swap = True
        while current_node:
            next_node = current_node.next
            if next_node:
                current_node.next = next_node.next
                next_node.next = current_node
                if previos_node:
                    previos_node.next = next_node
                previos_node = current_node
                if is_first_swap:
                    is_first_swap = False
                    head = next_node
            current_node = current_node.next
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """