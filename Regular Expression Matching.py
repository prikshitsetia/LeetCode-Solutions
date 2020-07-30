class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p=="":
            if s=="":
                return True
            else:
                return False
        if s!="" and (p[0]==s[0] or p[0]=="."):
            match=True
        else:
            match=False
        if len(p)>=2 and p[1]=="*":
            return (self.isMatch(s,p[2:]) or (match and self.isMatch(s[1:],p)))
        else:
            return match and self.isMatch(s[1:],p[1:])
        
                
                
                