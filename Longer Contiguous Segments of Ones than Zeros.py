class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones=0
        zeros=0
        maxones=0
        maxzeros=0
        for i in s:
            if i=='1':
                ones+=1
                maxzeros=max(maxzeros,zeros)
                zeros=0
            if i=='0':
                zeros+=1
                maxones=max(maxones,ones)
                ones=0
            maxzeros=max(maxzeros,zeros)
            maxones=max(maxones,ones)
        if maxones>maxzeros:
            return True
        return False