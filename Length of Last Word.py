class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        li=s.split(" ")
        if len(li)>0:
            return len(li[-1])
        else:
            return 0
        