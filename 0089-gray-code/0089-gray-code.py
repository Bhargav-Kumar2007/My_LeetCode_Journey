class Solution:
    def grayCode(self, n: int) -> List[int]:
        def graycode(n):
            if n==0:
                return ["0"]
            elif n==1:
                return ["0","1"]
            else:
                pre=graycode(n-1)
                suf=pre[::-1]
                prefix=["0"+i for i in pre]
                suffix=["1"+i for i in suf]
                return prefix+suffix
        def bintoint(lst):
            nl=[]
            for i in lst:
                x=0
                for j,k in enumerate(i[::-1]):
                    x+=int(k)*(2**j)
                nl.append(x)
            return nl
        return bintoint(graycode(n))        