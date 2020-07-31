class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        val=float('inf')
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                temp=nums[i]+nums[l]+nums[r]
                if abs(target-temp)<abs(val):
                    val=target-temp
                if temp<target:
                    l+=1
                else:
                    r-=1
            if val==0:
                break
        return target-val
                
        
        