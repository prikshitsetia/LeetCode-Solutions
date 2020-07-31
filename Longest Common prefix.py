class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        a=strs[0]
        new=""
        count=0
        for i in range(len(a)):
            for j in range(1,len(strs)):
                if i<len(strs[j]) and a[i]==strs[j][i]:
                    count+=1
                else:
                    return new
            new+=a[i]
        return new
                
                
                    
            
        
        