class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts=sorted(horizontalCuts)
        verticalCuts=sorted(verticalCuts)
        li=[horizontalCuts[0]]
        for i in range(1,len(horizontalCuts)):
            li.append(horizontalCuts[i]-horizontalCuts[i-1])
        li.append(h-horizontalCuts[-1])
        ki=[verticalCuts[0]]
        for i in range(1,len(verticalCuts)):
            ki.append(verticalCuts[i]-verticalCuts[i-1])
        ki.append(w-verticalCuts[-1])

        return (max(li)*max(ki))%1000000007