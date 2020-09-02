# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        l=sys.maxsize
        r=sys.maxsize
        if root.left:
            l=self.minDepth(root.left)+1
        if root.right:
            r=self.minDepth(root.right)+1
        return min(l,r)