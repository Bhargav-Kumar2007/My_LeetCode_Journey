class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lna=0
        for i in a:
            lna+=1
        lnb=0
        for i in b:
            lnb+=1
        n=lnb//lna if lnb//lna==lnb/lna else lnb//lna+1
        for i in range(2):
            if b in a*(n+i):
                return n+i
        return -1

         