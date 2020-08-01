class Solution:
    def helper(self,m,n,i,j,dp):
        if i>n-1 or j>m-1:
            return 0
        
        if dp[i][j]==-1:
            return 0
        
        if i==n-1 and j==m-1:
            dp[i][j]=1
            return 1

        if dp[i][j]!=-1 and dp[i][j]!=0:
            return dp[i][j]
        
        ans=self.helper(m,n,i+1,j,dp)+self.helper(m,n,i,j+1,dp)
        
        dp[i][j]=ans
        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in obstacleGrid:
            for j in range(len(i)):
                if i[j]==1:
                    i[j]=-1
        return self.helper(len(obstacleGrid[0]),len(obstacleGrid),0,0,obstacleGrid)