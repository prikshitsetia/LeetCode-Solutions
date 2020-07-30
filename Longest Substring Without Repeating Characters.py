class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=""
        ml=0
        result=0
        for i in s:
            if i not in a:
                a=a+i
                ml=ml+1
            else:
                x=a.index(i)
                a=a[x+1:]+i
                if a=="":
                    a=i
                result=max(result,ml)
                ml=len(a)
        result=max(result,ml)
        return result
        