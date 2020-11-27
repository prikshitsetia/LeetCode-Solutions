class Solution:
    def helper(self,candidates,target,start,li,result):
        if target<0:
            return
        if target==0:
            a=li[:]
            result.append(a)
            return
        for i in range(start,len(candidates)):
            if i==start or candidates[i]!=candidates[i-1]:
                li.append(candidates[i])
                print(i,start,li)
                self.helper(candidates,target-candidates[i],i+1,li,result)
                li.pop(-1)
        return result
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(candidates,target,0,[],[])