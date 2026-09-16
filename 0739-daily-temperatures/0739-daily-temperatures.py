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
            while ls:
                if temperatures[ls[-1][0]]<temperatures[i]:
                    a=ls.pop()
                    sd[a[0]]=n-a[1]
                    lsn-=1
                else:
                    break
            ls.append((i,n))
            lsn+=1
        res=[]
        for i in range(ln):
            res.append(sd.get(i,0))
        return res