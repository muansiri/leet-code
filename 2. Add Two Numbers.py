# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        val = 0
        result = ListNode(0)
        current_node = result
        while l1 or l2:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            current_node.next = ListNode(val % 10)
            current_node = current_node.next
            val = val // 10
        if val:
            current_node.next = ListNode(val)
        return result.next
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
