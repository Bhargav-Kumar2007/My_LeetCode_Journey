class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ln=0
        for _ in temperatures:
            ln+=1
        sd={}
        ls=[]
        lsn=0
        for i in range(ln):
            mx=0
            while ls:
                if temperatures[ls[-1]]<temperatures[i]:
                    a=ls.pop()
                    sd[a]=i-a
                    lsn-=1
                else:
                    break
            ls.append(i)
            lsn+=1
        res=[]
        for i in range(ln):
            res.append(sd.get(i,0))
        return res