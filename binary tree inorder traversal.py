# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.li=[]
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return
        self.inorderTraversal(root.left)
        self.li.append(root.val)
        self.inorderTraversal(root.right)
        return self.li