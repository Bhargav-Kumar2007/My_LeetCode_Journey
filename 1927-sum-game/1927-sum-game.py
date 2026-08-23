class Solution:
    def sumGame(self, num: str) -> bool:
        lq=0
        rq=0
        ls=0
        rs=0
        ln=0
        for _ in num:
            ln+=1
        for i in range(ln//2):
            try:
                ls+=int(num[i])
            except:
                lq+=1
        for i in range(ln//2,ln):
            try:
                rs+=int(num[i])
            except:
                rq+=1
        print(lq,ls,rq,rs)
        if lq == rq and ls==rs:
            return False
        if lq==rq and ls!=rs:
            return True
        if lq > rq:
            lq = lq - rq
            if lq%2:
                return True
            ls = ls + 4.5*lq
            if ls==rs:
                return False
            else:
                return True
        if lq < rq:
            rq = rq - lq
            if rq%2:
                return True
            rs = rs + 4.5*rq
            if ls==rs:
                return False
            else:
                return True

