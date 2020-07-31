class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        j=0
        start=0
        flag=0
        ans=-1
        i=0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                print(i)
                print(j)
                if j==0:
                    ans=i
                if j>0 and needle[0]==haystack[i] and flag==0:
                    start=i
                    flag=1
                    j+=1
                else:
                    j+=1
                if j==len(needle):
                    return ans 
            else:
                if flag==1:
                    i=start-1
                elif haystack[i]==needle[0]:
                    i=i-1
                else: 
                    if flag==1:
                        i=start-1
                flag=0
                j=0
            i+=1
        return -1
                    
                    
                
                