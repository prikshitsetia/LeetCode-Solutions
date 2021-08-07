class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count=0
        flag=0
        for i in range(len(nums)):
            if nums[i]>=left and nums[i]<=right:
                count+=1
                flag=1
            elif nums[i]>right:
                continue
            else:
                flag=0
            for j in range(i+1,len(nums)):
                if flag==1:
                    if nums[j]<=right:
                        count+=1
                    else:
                        break
                else:
                    if nums[j]>right:
                        break
                    elif nums[j]>=left and nums[j]<=right:
                        count+=1
                        flag=1
        return count
                        