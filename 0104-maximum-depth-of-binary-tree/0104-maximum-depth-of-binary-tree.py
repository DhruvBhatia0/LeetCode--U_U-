# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def maxlen(root):
            if root == None:
                return 0
            length = 1 + max(maxlen(root.left), maxlen(root.right))
            return length
            
        return maxlen(root)