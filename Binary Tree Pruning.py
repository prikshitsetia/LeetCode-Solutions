# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root.left==None and root.right==None:
            if root.val==1:
                return True
            return False
        leftOne=False
        rightOne=False
        if root.left:
            leftOne=self.helper(root.left)
        if root.right:
            rightOne=self.helper(root.right)
        if not leftOne:
            root.left=None
        if not rightOne:
            root.right=None
        if not (leftOne or rightOne):
            if root.val==1:
                return True
            return False
        return True
        
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not self.helper(root):
            return None
        return root