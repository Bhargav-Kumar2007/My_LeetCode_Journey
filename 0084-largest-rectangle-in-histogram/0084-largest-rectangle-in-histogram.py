class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ls=[]
        mx=0
        n=0
        for i in heights:
            ct=1
            while ls:
                if ls[-1][0]>=i:
                    tmp=ls.pop()
                    ct+=tmp[1]
                    cmx=tmp[0]*(ct-1)
                    if mx < cmx:
                        mx=cmx
                    n-=1
                else:
                    break
            ls.append((i,ct))
            n+=1
            if i==0:
                ls.pop()
                n-=1
        cnt=0
        for i in range(-1,-n-1,-1):
            cnt+=ls[i][1]
            cmx=ls[i][0]*cnt
            if cmx>mx:
                mx=cmx
        return mx