class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        li=[]
        for i in words:
            ptr={}
            s=set()
            j=0
            while j<len(i):
                if pattern[j] in ptr and ptr[pattern[j]]==i[j]:
                    j+=1
                    continue
                elif pattern[j] not in ptr and i[j] not in s:
                    s.add(i[j])
                    ptr[pattern[j]]=i[j]
                else:
                    break
                j+=1
            if j==len(pattern):
                li.append(i)
        return li