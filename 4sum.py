class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        li=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                low=j+1
                high=len(nums)-1
                while low<high:
                    if nums[i]+nums[j]+nums[low]+nums[high]<target:
                        low+=1
                    elif nums[i]+nums[j]+nums[low]+nums[high]>target:
                        high-=1
                    else:
                        li.append([nums[i],nums[j],nums[low],nums[high]])
                        low+=1
                        high-=1
                        while low<len(nums) and nums[low]==nums[low-1]:
                            low+=1
        return li
                
        