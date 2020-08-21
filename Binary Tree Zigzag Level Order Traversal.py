# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        cur=[]
        nex=[]
        cur.append(root)
        li=[]
        res=[]
        while len(cur)!=0 or len(nex)!=0:
            while len(cur)!=0:
                a=cur.pop(-1)
                li.append(a.val)
                if a.left:
                    nex.append(a.left)
                if a.right:
                    nex.append(a.right)
                    
            if len(li)!=0:
                res.append(li)
                li=[]
            while len(nex)!=0:
                b=nex.pop(-1)
                li.append(b.val)
                if b.right:
                    cur.append(b.right)
                if b.left:
                    cur.append(b.left)
            if len(li)!=0:
                res.append(li)
                li=[]
        return res
            