# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,preorder,inorder,prestart,preend,instart,inend):
        if instart>inend:
            return None
        root=TreeNode(preorder[prestart])
        rootindex=-1
        for i in range(instart,inend+1):
            if inorder[i]==preorder[prestart]:
                rootindex=i
                break
        lins=instart
        line=rootindex-1
        lpres=prestart+1
        lpree=line-lins+lpres
        rpres=lpree+1
        rpree=preend
        rins=rootindex+1
        rine=inend
        root.left=self.helper(preorder,inorder,lpres,lpree,lins,line)
        root.right=self.helper(preorder,inorder,rpres,rpree,rins,rine)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)