class Solution:
    def helper(self,triangle,i,j,di):
        if i==len(triangle):
            return 0
        if str(i)+" "+str(j) in di:
            return di[str(i)+" "+str(j)]
        
        ans=triangle[i][j]
        ans=ans+min(self.helper(triangle,i+1,j,di),self.helper(triangle,i+1,j+1,di))
        di[str(i)+" "+str(j)]=ans
        return ans
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.helper(triangle,0,0,{})