class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            muln=1
            x=n
            while x:
                muln*=(x%10)
                x=x//10
            if muln%t==0:
                return n
            n+=1
