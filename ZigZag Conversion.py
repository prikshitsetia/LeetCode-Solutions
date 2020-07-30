class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1:
            return s
        di={}
        m=n-2
        i=0
        while i<len(s):
            if i%(n+(n-2))==0:
                j=0
                while j<n and i<len(s):
                    if j in di:
                        di[j]+=s[i]
                    else:
                        di[j]=s[i]
                    i+=1
                    j+=1
                #i-=1
                continue
            else:
                di[m]+=s[i]
                m-=1
                if m==0:
                    m=n-2
            i+=1
                    
        ns=""
        print(di)
        for j in di.values():
            ns+=j
        return ns
                
                
        
        