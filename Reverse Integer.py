class Solution:
    def reverse(self, x: int) -> int:
        rem=0
        a=0
        z=x
        if x<0:
            x=-x
        while x>0:
            rem=x%10
            a=(a*10)+rem
            x=int(x/10)
        if a>2147483647:
            return 0
        if a<-2147483647:
            return 0
        if z>0:
            return a
        else:
            return -a
            
        