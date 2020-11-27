class Solution:
    def helper(self,candidates,target,start,li,result):
        print(target)
        if target<0:
            return
        if target==0:
            a=li[:]
            result.append(a)
            return
        for i in range(start,len(candidates)):
            li.append(candidates[i])
            self.helper(candidates,target-candidates[i],i,li,result)
            li.pop(-1)
        return result
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helper(candidates,target,0,[],[])
        