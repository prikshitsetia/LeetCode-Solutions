class Solution:
    def intToRoman(self, num: int) -> str:
        arr=[["I","II","III","IV","V","VI","VII","VIII","IX"],
             ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
             ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
             ["M","MM","MMM"]]
        place=0
        ans=""
        while num>0:
            rem=int(num%10)
            if rem!=0:
                ans=(arr[place])[rem-1]+ans
            num=num/10
            place+=1
        return ans
            
            
        
        