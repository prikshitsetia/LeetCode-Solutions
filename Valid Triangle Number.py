class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count=0
        nums=sorted(nums)
        for i in range(len(nums)-2):
            k=i+2
            for j in range(i+1,len(nums)):
                if nums[i]!=0:
                    while k<len(nums) and nums[i]+nums[j]>nums[k]:
                        k+=1
                    count=count+(k-j-1)
                    j=k
        return count