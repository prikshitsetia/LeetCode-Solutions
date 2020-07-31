class Solution:
    def longestValidParentheses(self, s: str) -> int:
        li=[0]
        for i in range(1,len(s)):
            if s[i]=="(":
                li.append(0)
            elif s[i]==")":
                if s[i-1]=="(":
                    if i>=2:
                        li.append(li[i-2]+2)
                    else:
                        li.append(2)
                elif (i-li[i-1]>0) and s[i-li[i-1]-1]=="(":
                    if i-li[i-1]>=2:
                        li.append(li[i-1]+li[i-li[i-1]-2]+2)
                    else:
                        li.append(li[i-1]+2)
                else:
                    li.append(0)
        if len(li)>0:
            return max(li)
        else:
            return 0
            
                    
                    