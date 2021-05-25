class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        li=[]
        flag=0
        flag1=0
        for i in tokens:
            if i=="+" or i=="-" or i=="*" or i=="/":
                a=li.pop(-1)
                b=li.pop(-1)
                if i=="+":
                    li.append(a+b)
                elif i=="-":
                    li.append(b-a)
                elif i=="*":
                    li.append(a*b)
                else:
                    li.append(int(b/a))
            else:
                li.append(int(i))
        return li[0]