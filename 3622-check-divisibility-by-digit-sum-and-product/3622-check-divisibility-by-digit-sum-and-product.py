class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sm=0
        prod=1
        cn=n
        while cn:
            tmp=cn%10
            sm+=tmp
            prod*=tmp
            cn=cn//10
        tot=sm+prod
        if n%tot:
            return False
        return True
