class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums=sorted(nums)
        maxi=-sys.maxsize-1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>maxi:
                maxi=nums[i]-nums[i-1]
        if maxi==-sys.maxsize-1:
            return 0
        return maxi
        