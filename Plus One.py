class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        car=1
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        i=len(digits)-1
        while i>=0:
            if digits[i]==9:
                digits[i]=0
                car=1
            else:
                digits[i]+=car
                car=0
                break
            i-=1
        if car==1:
            digits.insert(0,1)
        return digits
            
        