class Solution:
    def helper(self,nums,n,totalSum,dp):
        if totalSum==0:
            dp[n][totalSum]=True
            return True
        if n==0:
            dp[n][totalSum]=False
            return False
        if not dp[n][totalSum]==-1:
            return dp[n][totalSum]
        
        a=self.helper(nums,n-1,totalSum-nums[n-1],dp) or self.helper(nums,n-1,totalSum,dp)
        dp[n][totalSum]=a
        return a
    
    def canPartition(self, nums: List[int]) -> bool:
        if not sum(nums)%2==0:
            return False
        dp=[[-1 for j in range(int(sum(nums)/2)+1)] for i in range(len(nums)+1)]
        # return self.helper(nums,len(nums),int(sum(nums)/2),dp)
        
        totalSum=int(sum(nums)/2)
        
        for i in range(len(nums)+1):
            for j in range(totalSum+1):
                if j==0 and i==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=False
                elif j==0:
                    dp[i][j]=True
        for i in range(1,len(nums)+1):
            for j in range(1,totalSum+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(nums)][totalSum]