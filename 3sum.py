class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        li=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                temp=nums[i]+nums[l]+nums[r]
                if temp>0:
                    r-=1
                elif temp<0:
                    l+=1
                else:
                    li.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
            
        return li
                    
                
        