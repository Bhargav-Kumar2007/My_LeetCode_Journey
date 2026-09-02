class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ln=0
        f=0
        for i in s:
            if not f and i!=" ":
                ln+=1
                f=0
            if i!=" " and f:
                ln=1
                f=0
            if i==" ":
                f=1
        return ln