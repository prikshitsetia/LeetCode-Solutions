class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[0]==0:
            return 0
        jump=1
        farthest=nums[0]
        cur=nums[0]
        for i in range(1,len(nums)):
            if i==len(nums)-1:
                return jump
            farthest=max(farthest,i+nums[i])
            if i==cur:
                jump+=1
                cur=farthest
        return jump