class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1=len(s1)
        ls2=len(s2)
        f=False
        for i in range(ls2-ls1+1):
            lis1=list(s1)
            lis2=list(s2[i:i+ls1])
            if sorted(lis1)==sorted(lis2):
                return True