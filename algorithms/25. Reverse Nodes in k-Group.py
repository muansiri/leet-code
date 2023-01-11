# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        current_node, a = head, ListNode()
        tail = a
        while current_node:
            previous_node = None

            count = 1
            tmp_node = current_node
            for i in range(k - 1):
                if tmp_node.next:
                    tmp_node = tmp_node.next
                    count += 1
            equal_k = count == k
            if equal_k:
                for i in range(k):
                    if current_node:
                        tmp_node = current_node.next
                        current_node.next = previous_node
                        previous_node = current_node
                        current_node = tmp_node

            tail.next = previous_node if equal_k else current_node
            if not equal_k:
                break

            for i in range(k):
                tail = tail.next

        return a.next