class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=sorted(nums)
        print(nums)
        l=0
        maxl=0
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]!=nums[i+1] and nums[i]+1==nums[i+1]:
                    l+=1
            elif i+1<len(nums) and nums[i]==nums[i+1]:
                continue
            else:
                maxl=max(maxl,l)
                l=0
        return maxl+1