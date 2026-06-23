class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x=0
        while True:
            if x**2>c:
                return False
            elif (c-x**2)**0.5==int((c-x**2)**0.5):
                return True
            else:
                x+=1