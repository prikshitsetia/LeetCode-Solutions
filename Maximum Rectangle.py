class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxi=0
        if len(matrix)==0:
            return 0
        heights=[0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    heights[j]=heights[j]+1
                else:
                    heights[j]=0
            maxi=max(maxi,self.calculateHeight(heights))
        return maxi
    def calculateHeight(self,heights):
        print(heights)
        if len(heights)==0:
            return 0
        if len(heights)==1:
            return heights[0]
        li=[0]
        area=0
        for i in range(1,len(heights)):
            if heights[i]>=heights[li[-1]]:
                li.append(i)
            else:
                while len(li)!=0 and heights[li[-1]]>=heights[i]:
                    if len(li)>=2:
                        a=heights[li[-1]]*(i-li[-2]-1)
                        area=max(area,a)
                        li.pop(-1)
                        print(a)
                    else:
                        a=heights[li[-1]]*i
                        area=max(area,a)
                        li.pop(-1)
                        print(a)
                li.append(i)    
        while len(li)!=0:
            i=len(heights)
            if len(li)>=2:
                a=heights[li[-1]]*(i-li[-2]-1)
                area=max(area,a)
                li.pop(-1)
                print(a)
            else:
                a=heights[li[-1]]*i
                area=max(area,a)
                li.pop(-1)
                print(a)    
        return area
