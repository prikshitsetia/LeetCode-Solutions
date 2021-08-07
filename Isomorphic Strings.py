class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        di={}
        hs=set()
        st=""
        for i in range(len(s)):
            if s[i] in di:
                st=st+di[s[i]]
            else:
                if t[i] not in hs:
                    di[s[i]]=t[i]
                    st=st+t[i]
                    hs.add(t[i])
                else:
                    return False
        print(di)
        if st==t:
            return True
        return False
        