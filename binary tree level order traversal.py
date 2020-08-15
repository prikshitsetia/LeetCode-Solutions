# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,level,di):
        if str(level) in di:
            di[str(level)].append(root.val)
        else:
            di[str(level)]=[root.val]
        if root.left:
            self.preorder(root.left,level+1,di)
        if root.right:
            self.preorder(root.right,level+1,di)
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        di={}
        self.preorder(root,1,di)
        res=[]
        for i in di.values():
            res.append(i)
        return res