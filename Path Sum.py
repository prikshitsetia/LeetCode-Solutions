# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,sum):
        if root.left==None and root.right==None:
            if sum-root.val==0:
                return True
            return False
        a=False
        b=False
        if root.left:
            a=self.helper(root.left,sum-root.val)
        if root.right:
            b=self.helper(root.right,sum-root.val)
        if a or b:
            return True
        return False
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        return self.helper(root,sum)