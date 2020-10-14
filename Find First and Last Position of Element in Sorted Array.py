class Solution:
    def upperBound(self, nums, target):
        li = []
        left = 0
        ans = -1
        right = len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                ans = mid
                left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return ans

    def lowerBound(self, nums, target):
        li = []
        left = 0
        ans = -1
        right = len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                ans = mid
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.lowerBound(nums, target), self.upperBound(nums, target)]
