class Solution:
    di={}
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1==s2:
            self.di[s1+s2]=True
            return True
        if s1=="" or s2=="":
            self.di[s1+s2]=False
            return False
        if s1+s2 in self.di:
            return self.di[s1+s2]
        flag=False
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[(len(s2)-i):]) and self.isScramble(s1[i:],s2[:(len(s2)-i)]) or self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): #before or check if swap happens and after or checks if swap doesnot happens
                flag=True
        self.di[s1+s2]=flag
        return flag
            