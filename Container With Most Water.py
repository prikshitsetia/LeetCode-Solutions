class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        value=0
        while i<j:
            m=(j-i)*min(height[i],height[j])
            value=max(value,m)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
                    
        return value
                
            
            
            
            
            
            
        