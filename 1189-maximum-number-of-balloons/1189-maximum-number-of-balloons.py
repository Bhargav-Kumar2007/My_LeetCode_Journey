class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in text:
            if i in d:
                d[i]+=1
        d["l"]//=2
        d["o"]//=2
        dih = d["b"]
        for i in d:
            if d[i]<dih:
                dih = d[i]
        return dih