class Solution:
    def countAndSay(self, n: int) -> str:
        if n<1:
            return ""
        if n==1:
            return "1"
        
        s=self.countAndSay(n-1)
        i=0
        temp=""
        while i<len(s):
            j=i
            c=0
            while j<len(s) and s[j]==s[i] :
                j+=1
                c+=1
            temp=temp+str(c)+s[i]
            i=j
        return temp