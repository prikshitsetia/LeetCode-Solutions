# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self,left,right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        if left.val==right.val:
            if self.mirror(left.left,right.right) and self.mirror(left.right,right.left):
                return True
            return False
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.mirror(root,root)