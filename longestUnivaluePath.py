# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res=0
        
        def helper(root,prev):
            if not root: return 0
            left=helper(root.left,root.val)
            right=helper(root.right,root.val)
            self.res=max(self.res,left+right)
            return 1+max(left,right) if root.val==prev else 0
        
        helper(root,None)
        return self.res