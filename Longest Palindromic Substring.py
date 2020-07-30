class Solution:
    def check(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=0
        for i in range(len(s)):
            len1=self.check(s,i,i)
            len2=self.check(s,i,i+1)
            lenf=max(len1,len2)
            if lenf>end-start:
                start=i-int((lenf-1)/2)
                end=i+int(lenf/2)
        return s[start:end+1]
                            
    
    
        
        