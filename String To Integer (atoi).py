class Solution:
    def myAtoi(self, s: str) -> int:
        a=0
        flag=0
        s=s.lstrip()
        if s=="":
            return 0
        if s[0]=="-":
            flag=1
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]
        if s=="":
            return 0
        if s[0]<"0" and s[0]>"9":
            return 0
        for i in s:
            if i>="0" and i<="9":
                a=a*10+int(i)
            else:
                break
        if flag==1:
            a=-a
        if a <= -2147483648:
            return -2147483648
        elif a>=2147483647:
            return 2147483647
        else:
            return a
        