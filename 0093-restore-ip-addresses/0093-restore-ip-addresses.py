class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<4 or len(s)>12:
            return []
        l=[]
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    if s[i] and s[i:i+j] and s[i+j:i+j+k] and s[i+j+k:]:
                        l.append(s[:i]+"."+s[i:i+j]+"."+s[i+j:i+j+k]+"."+s[i+j+k:])
        nl=[]
        for i in l:
            x=i.split(".")
            f=True
            for j in x:
                if j[0]=="0" and j!="0":
                    f=False
                    break
                if 0>int(j) or int(j)>255:
                    f=False
                    break
            if f:
                nl.append(i)
        return nl