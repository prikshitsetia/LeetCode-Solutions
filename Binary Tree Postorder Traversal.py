# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,li):
        if root==None:
            return li
        self.helper(root.left,li)
        self.helper(root.right,li)
        li.append(root.val)
        return li
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helper(root,[])
        
        