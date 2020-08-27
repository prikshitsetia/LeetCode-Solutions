# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,di,level):
        if str(level) in di:
            di[str(level)].append(root.val)
        else:
            di[str(level)]=[root.val]
        if root.left:
            self.helper(root.left,di,level+1)
        if root.right:
            self.helper(root.right,di,level+1)
        return di
            
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        li=[]
        di=self.helper(root,{},1)
        for i in di.keys():
            li.append(di[i])
        return li[::-1]
            