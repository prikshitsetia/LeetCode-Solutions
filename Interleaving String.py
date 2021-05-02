class Solution:
    def helper(self,s1,i,s2,j,k,s3,li):
        if i==len(s1):
            if s2[j:]==s3[k:]:
                return True
            return False
        if j==len(s2):
            if s1[i:]==s3[k:]:
                return True
            return False
        if li[i][j]>=0:
            if li[i][j]==1:
                return True
            else:
                return False
        ans=False
        if s1[i]==s3[k] and self.helper(s1,i+1,s2,j,k+1,s3,li) or s2[j]==s3[k] and self.helper(s1,i,s2,j+1,k+1,s3,li):
            ans=True
        if ans==True:
            li[i][j]=1
        else:
            li[i][j]=0
        return li[i][j]
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        li=[[-1 for i in range(len(s2))] for j in range(len(s1))]
        return self.helper(s1,0,s2,0,0,s3,li)