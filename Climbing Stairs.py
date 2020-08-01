class Solution:
#     def helper(self,n,dp):
#         if n<0:
#             return 0
#         if n==0:
#             dp[n]=1
#             return 1
#         if dp[n]!=0:
#             return dp[n]
#         ans=self.helper(n-1,dp)+self.helper(n-2,dp)
#         dp[n]=ans
#         return dp[n]
    def climbStairs(self, n: int) -> int:
        dp=[0 for i in range(n+1)]
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]