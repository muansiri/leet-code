# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        nums = []
        for node in lists:
            while node:
                nums.append(node.val)
                node = node.next
        nums.sort()
        head = None
        current_node = None
        for num in nums:
            if head == None:
                head = ListNode(val=num, next=None)
                current_node = head
            else:
                current_node.next = ListNode(val=num, next=None)
                current_node = current_node.next
        return head


        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """