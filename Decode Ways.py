class Solution:
    def helper(self,s,dp,i):
        if s=="":
            return 1
        if s[0]=="0":
            return 0
        if s in dp:
            return dp[s]
        a=self.helper(s[1:],dp,i+1)
        dp[s]=a
        if len(s)>=2 and int(s[:2])<=26:
            a=a+self.helper(s[2:],dp,i+2)
            dp[s]=a
        return a
            
    def numDecodings(self, s: str) -> int:
        return self.helper(s,{},0)