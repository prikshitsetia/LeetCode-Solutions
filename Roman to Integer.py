class Solution:
    def romanToInt(self, s: str) -> int:
        n=0
        i=0
        while i<len(s):
            if s[i]=="I":
                if i+1<len(s):
                    if s[i+1]!="V":
                        if s[i+1]!="X":
                            n+=1
                            i+=1
                        else:
                            n+=9
                            i+=2
                    else:
                        n+=4
                        i+=2
                else:
                    n+=1
                    i+=1
            elif s[i]=="V":
                n+=5
                i+=1
            elif s[i]=="X":
                if i+1<len(s):
                    if s[i+1]!="L":
                        if s[i+1]!="C":
                            n+=10
                            i+=1
                        else:
                            n+=90
                            i+=2
                    else:
                        n+=40
                        i+=2
                else:
                    n+=10
                    i+=1
            elif s[i]=="L":
                n+=50
                i+=1
            elif s[i]=="C":
                if i+1<len(s):
                    if s[i+1]!="D":
                        if s[i+1]!="M":
                            n+=100
                            i+=1
                        else:
                            n+=900
                            i+=2
                    else:
                        n+=400
                        i+=2
                else:
                    n+=100
                    i+=1
            elif s[i]=="D":
                n+=500
                i+=1
            elif s[i]=="M":
                n+=1000
                i+=1
        return n
                        
                
                        
        