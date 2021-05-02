class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di={}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in di:
                di[temp].append(i)
            else:
                di[temp]=[i]
        final=[]
        for i in di.values():
            final.append(i)
        return(final)