class Solution:
#     def helper(self,word1,word2,i,j,dp):
#         if i==0 and j==0:
#             dp[i][j]=0
#             return 0
#         if i==0:
#             dp[i][j]=j
#             return j
#         if j==0:
#             dp[i][j]=i
#             return i
#         if dp[i][j]!=-1:
#             return dp[i][j]
#         if word1[i-1]==word2[j-1]: # Replace 
#             dp[i][j]=self.helper(word1,word2,i-1,j-1,dp)
#             return dp[i][j]
#         else:
            #Replace delete insert
#             dp[i][j]=min(self.helper(word1,word2,i-1,j-1,dp)+1,self.helper(word1,word2,i-1,j,dp)+1,self.helper(word1,word2,i,j-1,dp)+1)
#             return dp[i][j]
            
            
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        dp[0][0]=0
        for i in range(len(word1)+1):
            dp[i][0]=i
        for j in range(len(word2)+1):
            dp[0][j]=j
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[len(word1)][len(word2)]
    
        #return self.helper(word1,word2,len(word1),len(word2),dp)
        
        