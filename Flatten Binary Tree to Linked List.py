# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        a = None
        b = None
        if root.left:
            a = self.flatten(root.left)
        if root.right:
            b = self.flatten(root.right)
        root.left = None
        if a:
            root.right = a
            temp = root
            while temp.right != None:
                temp = temp.right
            temp.right = b
        elif b:
            root.right = b
        return root
