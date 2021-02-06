class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        li=[]
        s=""
        car=0
        k=0
        for i in range(len(num2)-1,-1,-1):
            for j in range(len(num1)-1,-1,-1):
                a=int(num1[j])
                b=int(num2[i])
                temp=(a*b)+car
                if j==0:
                    car=0
                    s=str(temp)+s
                else:
                    car=int(temp/10)
                    s=str(temp%10)+s
            for i in range(k):
                s=s+"0"
            li.append(s)
            print(li)
            s=""
            k+=1
        ans=0
        for i in li:
            ans=ans+int(i)
        return str(ans)