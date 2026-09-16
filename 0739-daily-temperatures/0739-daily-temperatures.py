class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ln=0
        for _ in temperatures:
            ln+=1
        sd={}
        ls=[]
        lsn=0
        n=0
        for i in range(ln):
            n+=1
            mx=0
            for j in range(-1,-lsn-1,-1):
                if temperatures[ls[j][0]]<temperatures[i]:
                    mx+=1
                else:
                    break
            for j in range(mx):
                a=ls.pop()
                lsn-=1
                sd[a[0]]=n-a[1]
            ls.append((i,n))
            lsn+=1
        res=[]
        for i in range(ln):
            res.append(sd.get(i,0))
        return res