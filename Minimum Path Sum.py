class Solution:
    def helper(self,m,n,i,j,grid,dp):
        if i==m-1 and j==n-1:
            dp[i][j]=grid[i][j]
            return grid[i][j]
        if i>m-1 or j>n-1:
            return sys.maxsize
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]=grid[i][j]+min(self.helper(m,n,i+1,j,grid,dp),self.helper(m,n,i,j+1,grid,dp))
        return dp[i][j]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        return self.helper(len(grid),len(grid[0]),0,0,grid,dp)
        