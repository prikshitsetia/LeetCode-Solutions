class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp=0
        for i in nums:
            if i==1:
                temp=1
                break
        if temp==1:
            if len(nums)==1:
                return 2
            for i in range(len(nums)):
                if nums[i]<=0 or nums[i]>len(nums):
                    nums[i]=1
            print(nums)
            temp=[i for i in nums]
            for i in range(len(nums)):
                if nums[nums[i]-1]>0:
                    temp[nums[i]-1]=-nums[nums[i]-1]
            print(temp)
            for i in range(len(nums)):
                if temp[i]>0:
                    return i+1
            return len(nums)+1
                
        else:
            return 1