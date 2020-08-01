class Solution:
    def helper(self,m,n,i,j,dp):

        if i==n-1 and j==m-1:
            dp[i][j]=1
            return 1
        
        if i>n-1 or j>m-1:
            return 0
        
        
        if dp[i][j]!=0:
            return dp[i][j]
        
        ans=self.helper(m,n,i+1,j,dp)+self.helper(m,n,i,j+1,dp)
        
        dp[i][j]=ans
        print(f"{i}{j}")
        for l in range(n):
            for b in range(m):
                print(dp[l][b],end=" ")
            print("\n")
        return dp[i][j]
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        return self.helper(m,n,0,0,dp)