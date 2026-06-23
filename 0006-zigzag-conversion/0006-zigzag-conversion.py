class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        r = True
        l=[[]for i in range(numRows)]
        x=-1
        for i in s:
            try:
                if r:
                    x+=1
                    l[x].append(i)
                else:
                    x-=1
                    l[x].append(i)
            except:
                if r:
                    x=-2
                    l[x].append(i)
                    r=False
                else:
                    x=1
                    l[x].append(i)
                    r=True
        z=""
        for i in l:
            for j in i:
                z+=j
        return z