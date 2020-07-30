class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        if (x%10)==0:
            return False
        else:
            n=0
            while x>n:
                n=n*10+(x%10)
                x=int(x/10)
            if x==n:
                return True
            else:
                if x==int(n/10):
                    return True
                else:
                    return False