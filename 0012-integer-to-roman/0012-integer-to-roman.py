class Solution:
    def intToRoman(self, num: int) -> str:
        def rezero(n,p):
            x=[("I","V"),("X","L"),("C","D"),("M",)]
            if 0<=n<4:
                return x[p][0]*n
            elif n==4:
                return x[p][0]+x[p][1]
            elif n==5:
                return x[p][1]
            elif n<9:
                return x[p][1]+(x[p][0]*(n-5))
            elif n==9:
                return x[p][0]+x[p+1][0]
        x=""
        j=len(str(num))-1
        try:
            for i in str(num):
                x+=rezero(int(i),j)
                j-=1
        except:
            pass
        return x