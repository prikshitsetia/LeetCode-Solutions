class Solution:
    def helper(self,s,p,i,j,dp):
        if i==len(s) and j==len(p):
            print("first \n")
            return True
        if i==len(s):
            for k in range(j,len(p)):
                if p[k]!="*":
                    return False
            print("second\n")
            return True
        if j==len(p) and i!=len(s):
            return False
        if dp[i][j]!=None:
            return dp[i][j]
        ans=False
        if p[j]=="?":
            if self.helper(s,p,i+1,j+1,dp):
                ans=True    
        elif p[j]=="*":
            if self.helper(s,p,i,j+1,dp):
                print("1\n")
                ans=True
            if self.helper(s,p,i+1,j,dp):
                print("2\n")
                ans=True
            if self.helper(s,p,i+1,j+1,dp):
                print("3\n")
                ans=True
        elif s[i]==p[j] and self.helper(s,p,i+1,j+1,dp):
                ans=True
        dp[i][j]=ans
        return ans
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[None for j in range(len(p))] for i in range(len(s))]
        return self.helper(s,p,0,0,dp)