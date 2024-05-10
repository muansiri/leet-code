# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        tail = ans
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                next_item = list1
                list1 = list1.next
            else:
                next_item = list2
                list2 = list2.next

            tail.next = next_item
            tail = next_item

        return ans.next
