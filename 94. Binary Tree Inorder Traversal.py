# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recursive(node, ans):
            if node:
                recursive(node.left, ans)
                ans.append(node.val)
                recursive(node.right, ans)
        recursive(root, ans)
        return ans
