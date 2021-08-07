import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def factorial(n):
            if n==0:
                return 1
            return math.factorial(n)
        li=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                a=int(factorial(i)/(factorial(j)*factorial(i-j)))
                temp.append(a)
            li.append(temp)
        return li
                      
        
        