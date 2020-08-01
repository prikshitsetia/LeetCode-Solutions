import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxl=-sys.maxsize
        temp=0
        for i in nums:
            temp=max(temp+i,i)
            maxl=max(maxl,temp)
        return maxl
                
        