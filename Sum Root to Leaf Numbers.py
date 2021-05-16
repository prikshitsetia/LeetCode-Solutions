# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        global fi
        fi=0
        def helper(root,s):
            if root==None:
                return
            if root.left==None and root.right==None:
                s=s+str(root.val)
                tmp=int(s)
                global fi
                fi=fi+tmp
                return 
            if root.left:
                helper(root.left,s+str(root.val))
            if root.right:
                helper(root.right,s+str(root.val))
        helper(root,"")
        return fi