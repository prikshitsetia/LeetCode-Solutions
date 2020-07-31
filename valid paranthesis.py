class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                li.append(i)
            else:
                if i==')':
                    if len(li)!=0 and li[-1]=='(':
                        pass
                    else:
                        return False
                elif i=="]":
                    if len(li)!=0 and li[-1]=='[':
                        pass
                    else:
                        return False
                elif i=="}":
                    if len(li)!=0 and li[-1]=="{":
                        pass
                    else:
                        return False
                li.pop(-1)
        if len(li)==0:
            return True
        else:
            return False
                    
                
        