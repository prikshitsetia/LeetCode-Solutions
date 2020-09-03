# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    li=[]
    temp=[]
    def helper(self,root,sum):
        print(self.temp)
        if root.left==None and root.right==None:
            self.temp.append(root.val)
            if sum-root.val==0:
                a=[]
                for i in self.temp:
                    a.append(i)
                self.li.append(a)
                self.temp.pop(-1)
                return True
            self.temp.pop(-1)
            return False
        a=False
        b=False
        self.temp.append(root.val)
        if root.left:
            a=self.helper(root.left,sum-root.val)
        if root.right:
            b=self.helper(root.right,sum-root.val)
        if len(self.temp)>0:
            self.temp.pop(-1)
        if a or b:
            return True
        return False
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root==None:
            return []
        self.li=[]
        self.temp=[]
        self.helper(root,sum)
        return self.li
        