# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root):
        if root == None: return 0
        l, r = self.recursive(root.left), self.recursive(root.right)
        if l == -1 or r == -1 or abs(l-r) > 1: return -1
        return 1 + max(l, r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root) >= 0
