# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,inorder,postorder,inStart,inEnd,postStart,postEnd):
        print(inStart)
        if inStart>inEnd:
            return None
        root=TreeNode(postorder[postEnd])
        rootIndex=-1
        for i in range(inStart,inEnd+1):
            if inorder[i]==postorder[postEnd]:
                rootIndex=i
                break
        inLeftStart=inStart
        inLeftEnd=rootIndex-1
        postLeftStart=postStart
        postLeftEnd=inLeftEnd-inLeftStart+postLeftStart
        inRightStart=rootIndex+1
        inRightEnd=inEnd
        postRightStart=postLeftEnd+1
        postRightEnd=postEnd-1
        
        root.left=self.helper(inorder,postorder,inLeftStart,inLeftEnd,postLeftStart,postLeftEnd)
        root.right=self.helper(inorder,postorder,inRightStart,inRightEnd,postRightStart,postRightEnd)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(inorder,postorder,0,len(inorder)-1,0,len(postorder)-1)
        