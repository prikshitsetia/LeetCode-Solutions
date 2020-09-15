# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, li):
        if root == None:
            return li
        li.append(root.val)
        self.preorder(root.left, li)
        self.preorder(root.right, li)
        return li

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.preorder(root, [])
