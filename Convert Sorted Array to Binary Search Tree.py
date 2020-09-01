
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,left,right,nums):
        if left>=right:
            return None
        mid=int((left+right)/2)
        root=TreeNode(nums[mid])
        root.left=self.helper(left,mid,nums)
        root.right=self.helper(mid+1,right,nums)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(0,len(nums),nums)
