class Solution:
    def customSortString(self, order: str, str: str) -> str:
        orderMap={}
        for i in order:
            orderMap[i]=order.index(i)
        strMap={}
        restOfChar=""
        for i in str:
            if i in orderMap:
                if orderMap[i] in strMap:
                    strMap[orderMap[i]]=strMap[orderMap[i]]+i
                else:
                    strMap[orderMap[i]]=i
            else:
                restOfChar=restOfChar+i
        result=""
        for i in range(len(strMap)):
            result+=strMap[i]
        result+=restOfChar
        return result